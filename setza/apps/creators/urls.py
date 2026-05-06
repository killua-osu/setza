from django.urls import path

from apps.discover.views import CreatorDiscoverView, CreatorOpportunityBrowseView
from apps.messaging.views import CreatorMessagesView

from .views import (
    CreatorCollaborationsView,
    CreatorDashboardView,
    CreatorProfileAnalyticsView,
    CreatorProfileRedirectView,
    CreatorProfileServicesView,
    CreatorServiceDetailView,
    CreatorServicesView,
)

app_name = "creator"

urlpatterns = [
    path("dashboard/", CreatorDashboardView.as_view(), name="dashboard"),
    path("discover/", CreatorDiscoverView.as_view(), name="discover"),
    path("messages/", CreatorMessagesView.as_view(), name="messages"),
    path("profile/", CreatorProfileRedirectView.as_view(), name="profile"),
    path("profile/services/", CreatorProfileServicesView.as_view(), name="profile_services"),
    path("profile/analytics/", CreatorProfileAnalyticsView.as_view(), name="profile_analytics"),
    path("services/", CreatorServicesView.as_view(), name="services"),
    path("services/<slug:slug>/", CreatorServiceDetailView.as_view(), name="service_detail"),
    path("collaborations/", CreatorCollaborationsView.as_view(), name="collaborations"),
    path("opportunities/", CreatorOpportunityBrowseView.as_view(), name="opportunities"),
]
