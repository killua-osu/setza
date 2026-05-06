from django.urls import path

from .views import BasicProfileView, ConnectAccountsView, RoleSelectionView

app_name = "onboarding"

urlpatterns = [
    path("role/", RoleSelectionView.as_view(), name="role"),
    path("profile/", BasicProfileView.as_view(), name="profile"),
    path("connect-accounts/", ConnectAccountsView.as_view(), name="connect_accounts"),
]
