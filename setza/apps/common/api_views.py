from copy import deepcopy

from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from pydantic import ValidationError

from apps.common.validation import pydantic_errors
from apps.discover.mappers import DiscoverFilterInput
from apps.messaging.mappers import MessageReplyInput

from .api_serializers import (
    BrandCardSerializer,
    ConnectedAccountSerializer,
    ConversationSerializer,
    CreatorCardSerializer,
    HealthSerializer,
    OpportunitySerializer,
    ProfileSerializer,
    ServiceSerializer,
)
from .mock_data import (
    get_brand_opportunities,
    get_brand_profile,
    get_connected_accounts,
    get_creator_profile,
    get_discover_cards,
    get_messages,
    get_opportunity,
    get_public_opportunities,
    get_service,
    get_services,
)


def _filter_cards(cards, query=None, platform=None):
    if query:
        query = query.lower()
        cards = [card for card in cards if query in card["name"].lower() or query in card["niche"].lower()]
    if platform:
        platform = platform.lower()
        cards = [card for card in cards if any(platform in item.lower() for item in card["platforms"])]
    return cards


def _resolve_thread(role, slug):
    messaging = get_messages(role)
    thread = next((item for item in messaging["conversations"] if item["slug"] == slug), messaging["conversations"][0])
    return deepcopy(thread)


class HealthAPIView(APIView):
    @extend_schema(responses=HealthSerializer)
    def get(self, request):
        return Response({"status": "ok", "app": "Setza"})


class CreatorDiscoverAPIView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter("q", str, description="Search by creator name or niche"),
            OpenApiParameter("platform", str, description="Filter by platform"),
        ],
        responses=CreatorCardSerializer(many=True),
    )
    def get(self, request):
        filters = DiscoverFilterInput.model_validate(request.GET.dict())
        return Response(_filter_cards(get_discover_cards("creators"), filters.q, filters.platform))


class BrandDiscoverAPIView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter("q", str, description="Search by brand name or niche"),
            OpenApiParameter("platform", str, description="Filter by platform"),
        ],
        responses=BrandCardSerializer(many=True),
    )
    def get(self, request):
        filters = DiscoverFilterInput.model_validate(request.GET.dict())
        return Response(_filter_cards(get_discover_cards("brands"), filters.q, filters.platform))


class CreatorProfileAPIView(APIView):
    @extend_schema(responses=ProfileSerializer)
    def get(self, request):
        return Response(get_creator_profile())


class BrandProfileAPIView(APIView):
    @extend_schema(responses=ProfileSerializer)
    def get(self, request):
        return Response(get_brand_profile())


class CreatorServicesAPIView(APIView):
    @extend_schema(responses=ServiceSerializer(many=True))
    def get(self, request):
        return Response(get_services())


class ServiceDetailAPIView(APIView):
    @extend_schema(responses=ServiceSerializer)
    def get(self, request, slug):
        return Response(get_service(slug))


class BrandOpportunitiesAPIView(APIView):
    @extend_schema(responses=OpportunitySerializer(many=True))
    def get(self, request):
        return Response(get_brand_opportunities())


class PublicOpportunitiesAPIView(APIView):
    @extend_schema(responses=OpportunitySerializer(many=True))
    def get(self, request):
        return Response(get_public_opportunities())


class MessagesListAPIView(APIView):
    @extend_schema(responses=ConversationSerializer(many=True))
    def get(self, request, role):
        return Response(get_messages(role)["conversations"])


class MessageThreadAPIView(APIView):
    @extend_schema(responses=ConversationSerializer)
    def get(self, request, role, slug):
        return Response(_resolve_thread(role, slug))


class MessageReplyAPIView(APIView):
    @extend_schema(request=MessageReplyInput, responses=ConversationSerializer)
    def post(self, request, role, slug):
        try:
            payload = MessageReplyInput.model_validate(request.data)
        except ValidationError as exc:
            field_errors, non_field_errors = pydantic_errors(exc)
            return Response(
                {"errors": field_errors, "non_field_errors": non_field_errors},
                status=400,
            )
        thread = _resolve_thread(role, slug)
        thread["messages"].append({"sender": "me", "time": "Just now", "body": payload.body})
        return Response(thread)


class ConnectedAccountsAPIView(APIView):
    @extend_schema(responses=ConnectedAccountSerializer(many=True))
    def get(self, request):
        return Response(get_connected_accounts())
