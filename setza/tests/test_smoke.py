import pytest

from apps.accounts.models import User


@pytest.fixture
def authenticated_client(client):
    user = User.objects.create_user(
        email="viewer@example.com",
        password="Password123",
        username="viewer",
        active_role="creator",
    )
    client.force_login(user)
    return client


@pytest.mark.parametrize(
    "url",
    [
        "/discover/",
        "/discover/brands/",
        "/discover/opportunities/",
        "/creator/dashboard/",
        "/creator/profile/services/",
        "/creator/profile/analytics/",
        "/creator/messages/",
        "/creator/services/",
        "/creator/services/reel-production/",
        "/creator/collaborations/",
        "/brand/dashboard/",
        "/brand/profile/opportunities/",
        "/brand/profile/analytics/",
        "/brand/messages/",
        "/brand/opportunities/",
        "/brand/opportunities/club-event-promotion-campaign/",
        "/brand/collaborations/",
        "/onboarding/connect-accounts/",
        "/settings/connected-accounts/",
    ],
)
@pytest.mark.django_db
def test_pages_render_for_authenticated_users(authenticated_client, url):
    response = authenticated_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_home_redirects_authenticated_users_to_dashboard(authenticated_client):
    response = authenticated_client.get("/")
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/creator/dashboard/")


@pytest.mark.django_db
def test_services_shortcut_redirects_authenticated_users(authenticated_client):
    response = authenticated_client.get("/services/")
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/creator/services/")


@pytest.mark.django_db
def test_auth_pages_render_for_guests(client):
    for url in ["/auth/sign-in/", "/auth/sign-up/", "/auth/forgot-password/"]:
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.parametrize("url", ["/", "/discover/", "/creator/dashboard/", "/brand/dashboard/", "/onboarding/connect-accounts/", "/services/"])
@pytest.mark.django_db
def test_protected_pages_redirect_guests_to_sign_in(client, url):
    response = client.get(url)
    assert response.status_code == 302
    assert "/auth/sign-in/" in response.headers["Location"]


@pytest.mark.django_db
def test_thread_partial_renders(authenticated_client):
    response = authenticated_client.get("/messages/thread/creator/violet-reds/", HTTP_HX_REQUEST="true")
    assert response.status_code == 200
    assert b"Violet Reds" in response.content


@pytest.mark.django_db
def test_send_message_partial_renders(authenticated_client):
    response = authenticated_client.post(
        "/messages/thread/creator/violet-reds/send/",
        {"body": "Testing thread response"},
        HTTP_HX_REQUEST="true",
    )
    assert response.status_code == 200
    assert b"Testing thread response" in response.content


@pytest.mark.django_db
def test_sign_up_creates_user_and_redirects(client):
    response = client.post(
        "/auth/sign-up/",
        {
            "email": "newcreator@example.com",
            "role": "creator",
            "password": "Password123",
            "confirm_password": "Password123",
        },
    )
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/onboarding/role/")
    assert User.objects.filter(email="newcreator@example.com").exists()


@pytest.mark.django_db
def test_sign_in_redirects_to_role_dashboard(client):
    User.objects.create_user(
        email="branduser@example.com",
        password="Password123",
        username="branduser",
        active_role="brand",
    )
    response = client.post(
        "/auth/sign-in/",
        {
            "email": "branduser@example.com",
            "password": "Password123",
        },
    )
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/brand/dashboard/")


@pytest.mark.django_db
def test_logout_redirects_to_sign_in(authenticated_client):
    response = authenticated_client.post("/auth/sign-out/")
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/auth/sign-in/")

    protected = authenticated_client.get("/creator/dashboard/")
    assert protected.status_code == 302
    assert "/auth/sign-in/" in protected.headers["Location"]
