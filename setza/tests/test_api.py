import pytest


@pytest.mark.parametrize(
    "url",
    [
        "/api/health/",
        "/api/schema/",
        "/api/docs/",
        "/api/discover/creators/",
        "/api/discover/brands/",
        "/api/creator/profile/",
        "/api/creator/services/",
        "/api/creator/services/reel-production/",
        "/api/brand/profile/",
        "/api/brand/opportunities/",
        "/api/opportunities/",
        "/api/messages/creator/threads/",
        "/api/messages/creator/threads/violet-reds/",
        "/api/connected-accounts/",
    ],
)
@pytest.mark.django_db
def test_api_endpoints_render(client, url):
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_api_message_reply(client):
    response = client.post("/api/messages/creator/threads/violet-reds/reply/", {"body": "Hello from Swagger"})
    assert response.status_code == 200
    assert response.json()["messages"][-1]["body"] == "Hello from Swagger"
