from pathlib import Path
from shutil import rmtree

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand, call_command
from django.test import Client
from django.urls import set_script_prefix

from apps.common.mock_data import get_brand_opportunities, get_services


STATIC_ROUTES = [
    ("/", "index.html", "creator"),
    ("/auth/sign-in/", "auth/sign-in/index.html", None),
    ("/auth/sign-up/", "auth/sign-up/index.html", None),
    ("/auth/forgot-password/", "auth/forgot-password/index.html", None),
    ("/creator/dashboard/", "creator/dashboard/index.html", "creator"),
    ("/creator/discover/", "creator/discover/index.html", "creator"),
    ("/creator/messages/", "creator/messages/index.html", "creator"),
    ("/creator/profile/services/", "creator/profile/services/index.html", "creator"),
    ("/creator/profile/analytics/", "creator/profile/analytics/index.html", "creator"),
    ("/creator/services/", "creator/services/index.html", "creator"),
    ("/creator/collaborations/", "creator/collaborations/index.html", "creator"),
    ("/creator/opportunities/", "creator/opportunities/index.html", "creator"),
    ("/brand/dashboard/", "brand/dashboard/index.html", "brand"),
    ("/brand/discover/", "brand/discover/index.html", "brand"),
    ("/brand/messages/", "brand/messages/index.html", "brand"),
    ("/brand/profile/opportunities/", "brand/profile/opportunities/index.html", "brand"),
    ("/brand/profile/analytics/", "brand/profile/analytics/index.html", "brand"),
    ("/brand/opportunities/", "brand/opportunities/index.html", "brand"),
    ("/brand/collaborations/", "brand/collaborations/index.html", "brand"),
    ("/discover/", "discover/index.html", "creator"),
    ("/discover/brands/", "discover/brands/index.html", "brand"),
    ("/discover/opportunities/", "discover/opportunities/index.html", "creator"),
    ("/opportunities/", "opportunities/index.html", "creator"),
    ("/settings/connected-accounts/", "settings/connected-accounts/index.html", "creator"),
]


class Command(BaseCommand):
    help = "Export the Django demo to static files for GitHub Pages."

    def add_arguments(self, parser):
        parser.add_argument(
            "--output",
            default=str(settings.BASE_DIR / "dist"),
            help="Directory to write the static Pages artifact into.",
        )

    def handle(self, *args, **options):
        output_dir = Path(options["output"]).resolve()
        if output_dir.exists():
            rmtree(output_dir)
        output_dir.mkdir(parents=True)

        base_path = getattr(settings, "GITHUB_PAGES_BASE_PATH", "")
        script_prefix = "/"
        set_script_prefix(script_prefix)

        call_command("collectstatic", interactive=False, verbosity=0)

        creator = self._demo_user("creator@setza.com", "creator")
        brand = self._demo_user("brand@setza.com", "brand")
        clients = {
            None: Client(),
            "creator": self._authenticated_client(creator),
            "brand": self._authenticated_client(brand),
        }

        routes = [*STATIC_ROUTES]
        routes.extend(
            (f"/creator/services/{service['slug']}/", f"creator/services/{service['slug']}/index.html", "creator")
            for service in get_services()
        )
        seen_opportunities = set()
        for opportunity in get_brand_opportunities():
            if opportunity["slug"] in seen_opportunities:
                continue
            seen_opportunities.add(opportunity["slug"])
            routes.append(
                (
                    f"/brand/opportunities/{opportunity['slug']}/",
                    f"brand/opportunities/{opportunity['slug']}/index.html",
                    "brand",
                )
            )

        for url, destination, role in routes:
            self._write_route(output_dir, clients[role], url, destination, base_path)

        (output_dir / ".nojekyll").write_text("", encoding="utf-8")
        self.stdout.write(self.style.SUCCESS(f"Exported GitHub Pages site to {output_dir}"))

    def _demo_user(self, email, role):
        User = get_user_model()
        user, _created = User.objects.get_or_create(
            email=email,
            defaults={"username": email.split("@")[0], "active_role": role},
        )
        if user.active_role != role:
            user.active_role = role
            user.save(update_fields=["active_role"])
        return user

    def _authenticated_client(self, user):
        client = Client()
        client.force_login(user)
        return client

    def _write_route(self, output_dir, client, url, destination, base_path):
        request_url = url
        response = client.get(request_url, follow=True)
        if response.status_code != 200:
            raise RuntimeError(f"Could not export {request_url}: HTTP {response.status_code}")

        target = output_dir / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        content = response.content.decode(response.charset or "utf-8")
        if base_path:
            prefix = f"/{base_path}/"
            content = content.replace('href="/', f'href="{prefix}')
            content = content.replace('src="/', f'src="{prefix}')
            content = content.replace('action="/', f'action="{prefix}')
            content = content.replace('hx-get="/', f'hx-get="{prefix}')
            content = content.replace('hx-post="/', f'hx-post="{prefix}')
        target.write_text(content, encoding="utf-8")
        self.stdout.write(f"exported {url} -> {target.relative_to(output_dir)}")
