from django.urls import path

from apps.discover.views import BrandDiscoverView
from apps.messaging.views import BrandMessagesView

from .views import (
    BrandCollaborationsView,
    BrandDashboardView,
    BrandOpportunitiesView,
    BrandOpportunityDetailView,
    BrandProfileAnalyticsView,
    BrandProfileOpportunitiesView,
    BrandProfileRedirectView,
)

app_name = "brand"

urlpatterns = [
    path("dashboard/", BrandDashboardView.as_view(), name="dashboard"),
    path("discover/", BrandDiscoverView.as_view(), name="discover"),
    path("messages/", BrandMessagesView.as_view(), name="messages"),
    path("profile/", BrandProfileRedirectView.as_view(), name="profile"),
    path("profile/opportunities/", BrandProfileOpportunitiesView.as_view(), name="profile_opportunities"),
    path("profile/analytics/", BrandProfileAnalyticsView.as_view(), name="profile_analytics"),
    path("opportunities/", BrandOpportunitiesView.as_view(), name="opportunities"),
    path("opportunities/<slug:slug>/", BrandOpportunityDetailView.as_view(), name="opportunity_detail"),
    path("collaborations/", BrandCollaborationsView.as_view(), name="collaborations"),
]
