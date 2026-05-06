from django.urls import path

from .views import ServicesRedirectView

app_name = "services"

urlpatterns = [
    path("", ServicesRedirectView.as_view(), name="root"),
]
