from django.urls import path

from .views import PublicOpportunitiesView

app_name = "opportunities"

urlpatterns = [
    path("", PublicOpportunitiesView.as_view(), name="browse"),
]
