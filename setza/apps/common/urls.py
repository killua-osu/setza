from django.urls import path

from .views import AppEntryRedirectView

urlpatterns = [
    path("", AppEntryRedirectView.as_view(), name="home"),
]
