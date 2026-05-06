from django.views.generic import TemplateView

from apps.common.mock_data import get_connected_accounts
from apps.common.viewmixins import SetzaPageMixin


class ConnectedAccountsSettingsView(SetzaPageMixin):
    role = "creator"
    active_nav = "dashboard"
    active_sidebar = "profile"
    template_name = "pages/settings/connected_accounts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["connected_accounts"] = get_connected_accounts()
        return context

# Create your views here.
