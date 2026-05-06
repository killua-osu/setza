from rest_framework import serializers


class HealthSerializer(serializers.Serializer):
    status = serializers.CharField()
    app = serializers.CharField()


class CreatorCardSerializer(serializers.Serializer):
    slug = serializers.SlugField()
    name = serializers.CharField()
    location = serializers.CharField()
    platforms = serializers.ListField(child=serializers.CharField())
    niche = serializers.CharField()
    description = serializers.CharField()
    followers = serializers.CharField()
    reach = serializers.CharField()
    engagement = serializers.CharField()


class BrandCardSerializer(serializers.Serializer):
    slug = serializers.SlugField()
    name = serializers.CharField()
    location = serializers.CharField()
    platforms = serializers.ListField(child=serializers.CharField())
    niche = serializers.CharField()
    description = serializers.CharField()
    campaign_engage = serializers.CharField()
    campaign_frequency = serializers.CharField()
    event_footfall = serializers.CharField()


class ServiceSerializer(serializers.Serializer):
    slug = serializers.SlugField()
    title = serializers.CharField()
    price = serializers.CharField()
    description = serializers.CharField()
    turnaround = serializers.CharField()
    concepts = serializers.CharField()
    revisions = serializers.CharField()
    platforms = serializers.ListField(child=serializers.CharField())
    deliverables = serializers.ListField(child=serializers.CharField())


class OpportunitySerializer(serializers.Serializer):
    slug = serializers.SlugField()
    title = serializers.CharField()
    brand = serializers.CharField()
    budget = serializers.CharField()
    followers_target = serializers.CharField()
    engagement_requirement = serializers.CharField()
    date = serializers.CharField()
    platforms = serializers.ListField(child=serializers.CharField())
    overview = serializers.CharField()
    deliverables = serializers.ListField(child=serializers.CharField())
    location = serializers.CharField()


class ProfileSerializer(serializers.Serializer):
    slug = serializers.SlugField()
    name = serializers.CharField()
    role = serializers.CharField()
    description = serializers.CharField()
    location = serializers.CharField()
    status_tags = serializers.ListField(child=serializers.CharField())
    traits = serializers.ListField(child=serializers.CharField())
    analytics = serializers.JSONField(required=False)
    services = ServiceSerializer(many=True, required=False)
    opportunities = OpportunitySerializer(many=True, required=False)


class ConversationMessageSerializer(serializers.Serializer):
    sender = serializers.CharField()
    time = serializers.CharField()
    body = serializers.CharField()


class ConversationSerializer(serializers.Serializer):
    slug = serializers.SlugField()
    name = serializers.CharField()
    type = serializers.CharField()
    meta = serializers.CharField()
    metric = serializers.CharField(allow_blank=True)
    context = serializers.CharField()
    preview = serializers.CharField()
    date = serializers.CharField()
    messages = ConversationMessageSerializer(many=True, required=False)


class ConnectedAccountSerializer(serializers.Serializer):
    provider = serializers.CharField()
    status = serializers.CharField()
    username = serializers.CharField()
    scopes = serializers.ListField(child=serializers.CharField())
    last_synced = serializers.CharField()
    token_state = serializers.CharField()
    copy = serializers.CharField()
