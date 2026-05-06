from django.urls import path

from .views import BrandDiscoverView, CreatorDiscoverView, CreatorOpportunityBrowseView

app_name = "discover"

urlpatterns = [
    path("", CreatorDiscoverView.as_view(), name="creator_discover"),
    path("brands/", BrandDiscoverView.as_view(), name="brand_discover"),
    path("opportunities/", CreatorOpportunityBrowseView.as_view(), name="creator_opportunities"),
]
