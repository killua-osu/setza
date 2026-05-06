from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .api_views import (
    BrandDiscoverAPIView,
    BrandOpportunitiesAPIView,
    BrandProfileAPIView,
    ConnectedAccountsAPIView,
    CreatorDiscoverAPIView,
    CreatorProfileAPIView,
    CreatorServicesAPIView,
    HealthAPIView,
    MessageReplyAPIView,
    MessageThreadAPIView,
    MessagesListAPIView,
    PublicOpportunitiesAPIView,
    ServiceDetailAPIView,
)

app_name = "api"

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="api:schema"), name="docs"),
    path("health/", HealthAPIView.as_view(), name="health"),
    path("discover/creators/", CreatorDiscoverAPIView.as_view(), name="discover_creators"),
    path("discover/brands/", BrandDiscoverAPIView.as_view(), name="discover_brands"),
    path("creator/profile/", CreatorProfileAPIView.as_view(), name="creator_profile"),
    path("creator/services/", CreatorServicesAPIView.as_view(), name="creator_services"),
    path("creator/services/<slug:slug>/", ServiceDetailAPIView.as_view(), name="service_detail"),
    path("brand/profile/", BrandProfileAPIView.as_view(), name="brand_profile"),
    path("brand/opportunities/", BrandOpportunitiesAPIView.as_view(), name="brand_opportunities"),
    path("opportunities/", PublicOpportunitiesAPIView.as_view(), name="public_opportunities"),
    path("messages/<str:role>/threads/", MessagesListAPIView.as_view(), name="message_threads"),
    path("messages/<str:role>/threads/<slug:slug>/", MessageThreadAPIView.as_view(), name="message_thread"),
    path("messages/<str:role>/threads/<slug:slug>/reply/", MessageReplyAPIView.as_view(), name="message_reply"),
    path("connected-accounts/", ConnectedAccountsAPIView.as_view(), name="connected_accounts"),
]
