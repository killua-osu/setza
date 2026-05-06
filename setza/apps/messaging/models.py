from django.conf import settings
from django.db import models

from apps.common.choices import ConversationType
from apps.common.models import TimeStampedModel


class Conversation(TimeStampedModel):
    creator_profile = models.ForeignKey(
        "accounts.CreatorProfile",
        on_delete=models.CASCADE,
        related_name="creator_conversations",
    )
    brand_profile = models.ForeignKey(
        "accounts.BrandProfile",
        on_delete=models.CASCADE,
        related_name="brand_conversations",
    )
    topic_type = models.CharField(max_length=20, choices=ConversationType.choices, default=ConversationType.SERVICE)
    topic_label = models.CharField(max_length=180, blank=True)
    service = models.ForeignKey(
        "services.Service",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="conversations",
    )
    opportunity = models.ForeignKey(
        "opportunities.Opportunity",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="conversations",
    )
    collaboration = models.ForeignKey(
        "collaborations.Collaboration",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="conversations",
    )
    last_message_preview = models.CharField(max_length=255, blank=True)
    last_message_at = models.DateTimeField(null=True, blank=True)
    unread_count_creator = models.PositiveIntegerField(default=0)
    unread_count_brand = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("-last_message_at", "-updated_at")

    def __str__(self):
        return self.topic_label or f"{self.creator_profile} / {self.brand_profile}"


class Message(TimeStampedModel):
    conversation = models.ForeignKey(
        "messaging.Conversation",
        on_delete=models.CASCADE,
        related_name="messages",
    )
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="messages")
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    is_system = models.BooleanField(default=False)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return f"{self.sender} @ {self.created_at:%Y-%m-%d %H:%M}"

# Create your models here.
