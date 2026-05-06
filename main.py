import argparse
import os
import subprocess
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = ROOT_DIR / "setza"


def parse_args():
    parser = argparse.ArgumentParser(description="Run Setza locally with one command.")
    parser.add_argument("--host", default=os.getenv("SETZA_HOST", "127.0.0.1"))
    parser.add_argument("--port", default=os.getenv("SETZA_PORT", "8000"))
    parser.add_argument("--skip-migrate", action="store_true")
    parser.add_argument("--skip-seed", action="store_true")
    parser.add_argument("--no-server", action="store_true", help="Run setup only, then exit.")
    return parser.parse_args()


def bootstrap_django():
    sys.path.insert(0, str(PROJECT_DIR))
    os.chdir(PROJECT_DIR)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    import django

    django.setup()


def main():
    args = parse_args()
    bootstrap_django()

    from django.core.management import call_command

    manage_script = PROJECT_DIR / "manage.py"

    if not args.skip_migrate:
        call_command("migrate", interactive=False)

    if not args.skip_seed:
        call_command("seed_demo_data")

    if args.no_server:
        print("Setza setup complete.")
        print("Swagger UI: http://%s:%s/api/docs/" % (args.host, args.port))
        return

    print("Starting Setza on http://%s:%s/" % (args.host, args.port))
    print("Swagger UI available at http://%s:%s/api/docs/" % (args.host, args.port))
    server_command = [
        sys.executable,
        str(manage_script),
        "runserver",
        f"{args.host}:{args.port}",
    ]
    raise SystemExit(subprocess.run(server_command, cwd=PROJECT_DIR, check=False).returncode)


if __name__ == "__main__":
    main()
