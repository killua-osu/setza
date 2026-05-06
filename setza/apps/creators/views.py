from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView

from apps.common.mock_data import (
    get_collaborations,
    get_creator_profile,
    get_dashboard,
    get_service,
    get_service_applications,
    get_services,
)
from apps.common.viewmixins import SetzaPageMixin
from apps.discover.views import CreatorDiscoverView, CreatorOpportunityBrowseView


class CreatorDashboardView(SetzaPageMixin):
    role = "creator"
    active_nav = "dashboard"
    active_sidebar = "overview"
    template_name = "pages/creator/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dashboard"] = get_dashboard("creator")
        return context


class CreatorProfileRedirectView(LoginRequiredMixin, RedirectView):
    pattern_name = "creator:profile_services"
    permanent = False


class CreatorProfileServicesView(SetzaPageMixin):
    role = "creator"
    active_nav = "dashboard"
    active_sidebar = "profile"
    template_name = "pages/creator/profile_services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = get_creator_profile()
        context["active_profile_tab"] = "services"
        context["profile_tabs"] = [
            {"key": "analytics", "label": "Analytics", "url": "/creator/profile/analytics/"},
            {"key": "services", "label": "Services", "url": "/creator/profile/services/"},
        ]
        return context


class CreatorProfileAnalyticsView(SetzaPageMixin):
    role = "creator"
    active_nav = "dashboard"
    active_sidebar = "profile"
    template_name = "pages/creator/profile_analytics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = get_creator_profile()
        context["active_profile_tab"] = "analytics"
        context["profile_tabs"] = [
            {"key": "analytics", "label": "Analytics", "url": "/creator/profile/analytics/"},
            {"key": "services", "label": "Services", "url": "/creator/profile/services/"},
        ]
        return context


class CreatorServicesView(SetzaPageMixin):
    role = "creator"
    active_nav = "dashboard"
    active_sidebar = "services"
    template_name = "pages/creator/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = get_services()[:3]
        context["dashboard"] = {"stats": [{"label": "Active Services", "value": 4, "icon": "gift"}, {"label": "Total Inquiries", "value": 9, "icon": "users"}]}
        return context


class CreatorServiceDetailView(SetzaPageMixin):
    role = "creator"
    active_nav = "dashboard"
    active_sidebar = "services"
    template_name = "pages/creator/service_detail.html"

    def get_switch_kwargs(self):
        return {"creator": {"slug": self.kwargs["slug"]}, "brand": {"slug": "club-event-promotion-campaign"}}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = get_service(self.kwargs["slug"])
        context["applications"] = get_service_applications()
        return context


class CreatorCollaborationsView(SetzaPageMixin):
    role = "creator"
    active_nav = "dashboard"
    active_sidebar = "collaborations"
    template_name = "pages/creator/collaborations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collaborations"] = get_collaborations("creator")
        return context

# Create your views here.
