from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView

from apps.discover.views import CreatorOpportunityBrowseView


class PublicOpportunitiesView(CreatorOpportunityBrowseView):
    pass


class RootOpportunityRedirectView(LoginRequiredMixin, RedirectView):
    pattern_name = "discover:creator_opportunities"
    permanent = False
