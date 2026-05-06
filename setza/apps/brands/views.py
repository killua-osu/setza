from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView

from apps.common.mock_data import (
    get_brand_opportunities,
    get_brand_profile,
    get_collaborations,
    get_dashboard,
    get_opportunity,
    get_opportunity_applications,
)
from apps.common.viewmixins import SetzaPageMixin
from apps.discover.views import BrandDiscoverView


class BrandDashboardView(SetzaPageMixin):
    role = "brand"
    active_nav = "dashboard"
    active_sidebar = "overview"
    template_name = "pages/brand/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dashboard"] = get_dashboard("brand")
        return context


class BrandProfileRedirectView(LoginRequiredMixin, RedirectView):
    pattern_name = "brand:profile_opportunities"
    permanent = False


class BrandProfileOpportunitiesView(SetzaPageMixin):
    role = "brand"
    active_nav = "dashboard"
    active_sidebar = "profile"
    template_name = "pages/brand/profile_opportunities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = get_brand_profile()
        context["active_profile_tab"] = "opportunities"
        context["profile_tabs"] = [
            {"key": "analytics", "label": "Analytics", "url": "/brand/profile/analytics/"},
            {"key": "opportunities", "label": "Opportunities", "url": "/brand/profile/opportunities/"},
        ]
        return context


class BrandProfileAnalyticsView(SetzaPageMixin):
    role = "brand"
    active_nav = "dashboard"
    active_sidebar = "profile"
    template_name = "pages/brand/profile_analytics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = get_brand_profile()
        context["active_profile_tab"] = "analytics"
        context["profile_tabs"] = [
            {"key": "analytics", "label": "Analytics", "url": "/brand/profile/analytics/"},
            {"key": "opportunities", "label": "Opportunities", "url": "/brand/profile/opportunities/"},
        ]
        return context


class BrandOpportunitiesView(SetzaPageMixin):
    role = "brand"
    active_nav = "opportunities"
    active_sidebar = "opportunities"
    template_name = "pages/brand/opportunities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["opportunities"] = get_brand_opportunities()
        context["summary_stats"] = [
            {"label": "Active Opportunities", "value": 4, "icon": "gift"},
            {"label": "Total Applications", "value": 6, "icon": "users"},
        ]
        return context


class BrandOpportunityDetailView(SetzaPageMixin):
    role = "brand"
    active_nav = "opportunities"
    active_sidebar = "opportunities"
    template_name = "pages/brand/opportunity_detail.html"

    def get_switch_kwargs(self):
        return {"creator": {"slug": "reel-production"}, "brand": {"slug": self.kwargs["slug"]}}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["opportunity"] = get_opportunity(self.kwargs["slug"])
        context["applications"] = get_opportunity_applications()
        return context


class BrandCollaborationsView(SetzaPageMixin):
    role = "brand"
    active_nav = "dashboard"
    active_sidebar = "collaborations"
    template_name = "pages/brand/collaborations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["collaborations"] = get_collaborations("brand")
        return context

# Create your views here.
