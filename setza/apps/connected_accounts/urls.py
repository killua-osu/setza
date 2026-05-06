from django.urls import path

from .views import ConnectedAccountsSettingsView

app_name = "connected_accounts"

urlpatterns = [
    path("connected-accounts/", ConnectedAccountsSettingsView.as_view(), name="connected_accounts"),
]
