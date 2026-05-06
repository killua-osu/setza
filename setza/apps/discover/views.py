from django.views.generic import TemplateView

from apps.common.mock_data import DISCOVER_FILTERS, get_discover_cards, get_public_opportunities
from apps.common.viewmixins import SetzaPageMixin

from .mappers import DiscoverFilterInput


class BaseDiscoverView(SetzaPageMixin):
    template_name = "pages/discover/discover.html"
    active_nav = "discover"
    discover_kind = "creators"

    def get_template_names(self):
        if self.request.headers.get("HX-Request"):
            return ["partials/discover_grid.html"]
        return [self.template_name]

    def _filter_cards(self, cards, filters):
        query = filters.q.lower()
        platform = filters.platform.lower()
        if query:
            cards = [card for card in cards if query in card["name"].lower() or query in card["niche"].lower()]
        if platform:
            cards = [card for card in cards if any(platform in item.lower() for item in card["platforms"])]
        return cards

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filters = DiscoverFilterInput.model_validate(self.request.GET.dict())
        context["filters"] = DISCOVER_FILTERS
        context["filter_values"] = filters.model_dump()
        context["discover_kind"] = self.discover_kind
        context["cards"] = self._filter_cards(get_discover_cards(self.discover_kind), filters)
        context["card_component"] = (
            "components/discover_creator_card.html"
            if self.discover_kind == "creators"
            else "components/discover_brand_card.html"
        )
        return context


class CreatorDiscoverView(BaseDiscoverView):
    role = "creator"
    discover_kind = "creators"


class BrandDiscoverView(BaseDiscoverView):
    role = "brand"
    discover_kind = "brands"


class CreatorOpportunityBrowseView(SetzaPageMixin):
    role = "creator"
    active_nav = "opportunities"
    template_name = "pages/discover/opportunities.html"

    def get_template_names(self):
        if self.request.headers.get("HX-Request"):
            return ["partials/opportunity_list.html"]
        return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_values"] = DiscoverFilterInput.model_validate(self.request.GET.dict()).model_dump()
        context["filters"] = DISCOVER_FILTERS
        context["opportunities"] = get_public_opportunities()
        return context
