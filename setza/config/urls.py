from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.common.api_urls")),
    path("", include("apps.common.urls")),
    path("auth/", include("apps.accounts.urls")),
    path("onboarding/", include("apps.onboarding.urls")),
    path("creator/", include("apps.creators.urls")),
    path("brand/", include("apps.brands.urls")),
    path("discover/", include("apps.discover.urls")),
    path("messages/", include("apps.messaging.urls")),
    path("opportunities/", include("apps.opportunities.urls")),
    path("services/", include("apps.services.urls")),
    path("settings/", include("apps.connected_accounts.urls")),
]
