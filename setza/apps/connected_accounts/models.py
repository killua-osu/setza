from django.conf import settings
from django.db import models

from apps.common.choices import ConnectionStatus, DataSourceType, PlatformType, TokenStatus, VerificationState
from apps.common.models import TimeStampedModel


class ConnectedAccount(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="connected_accounts")
    provider = models.CharField(max_length=32, choices=PlatformType.choices)
    provider_account_id = models.CharField(max_length=128)
    username = models.CharField(max_length=120, blank=True)
    profile_image_url = models.URLField(blank=True)
    access_token_encrypted = models.TextField(blank=True)
    refresh_token_encrypted = models.TextField(blank=True)
    token_expires_at = models.DateTimeField(null=True, blank=True)
    scopes = models.JSONField(default=list, blank=True)
    status = models.CharField(max_length=32, choices=ConnectionStatus.choices, default=ConnectionStatus.NOT_CONNECTED)
    token_status = models.CharField(max_length=32, choices=TokenStatus.choices, default=TokenStatus.ACTIVE)
    connected_at = models.DateTimeField(null=True, blank=True)
    last_synced_at = models.DateTimeField(null=True, blank=True)
    last_error = models.TextField(blank=True)

    class Meta:
        unique_together = ("user", "provider", "provider_account_id")
        ordering = ("user", "provider")

    def __str__(self):
        return f"{self.user.email} - {self.provider}"


class PlatformProfile(TimeStampedModel):
    connected_account = models.OneToOneField(
        "connected_accounts.ConnectedAccount",
        on_delete=models.CASCADE,
        related_name="platform_profile",
    )
    display_name = models.CharField(max_length=160)
    bio = models.TextField(blank=True)
    follower_count = models.PositiveIntegerField(default=0)
    reach_count = models.PositiveIntegerField(default=0)
    engagement_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    source_type = models.CharField(max_length=32, choices=DataSourceType.choices, default=DataSourceType.CONNECTED_PLATFORM)
    verification_state = models.CharField(max_length=32, choices=VerificationState.choices, default=VerificationState.VERIFIED)
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.display_name


class PlatformMetricsSnapshot(TimeStampedModel):
    platform_profile = models.ForeignKey(
        "connected_accounts.PlatformProfile",
        on_delete=models.CASCADE,
        related_name="snapshots",
    )
    captured_at = models.DateTimeField()
    follower_count = models.PositiveIntegerField(default=0)
    total_reach = models.PositiveIntegerField(default=0)
    engagement_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    account_engaged = models.PositiveIntegerField(default=0)
    hook_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    verification_state = models.CharField(max_length=32, choices=VerificationState.choices, default=VerificationState.VERIFIED)
    source_type = models.CharField(max_length=32, choices=DataSourceType.choices, default=DataSourceType.CONNECTED_PLATFORM)
    payload = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ("-captured_at",)

    def __str__(self):
        return f"{self.platform_profile.display_name} @ {self.captured_at:%Y-%m-%d}"


class PlatformMedia(TimeStampedModel):
    platform_profile = models.ForeignKey(
        "connected_accounts.PlatformProfile",
        on_delete=models.CASCADE,
        related_name="media_items",
    )
    title = models.CharField(max_length=160)
    media_type = models.CharField(max_length=64)
    section = models.CharField(max_length=64, blank=True)
    thumbnail_theme = models.CharField(max_length=80, blank=True)
    thumbnail_url = models.URLField(blank=True)
    external_url = models.URLField(blank=True)
    view_count = models.PositiveIntegerField(default=0)
    verification_state = models.CharField(max_length=32, choices=VerificationState.choices, default=VerificationState.VERIFIED)
    source_type = models.CharField(max_length=32, choices=DataSourceType.choices, default=DataSourceType.CONNECTED_PLATFORM)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class WebhookEvent(TimeStampedModel):
    provider = models.CharField(max_length=32, choices=PlatformType.choices)
    event_type = models.CharField(max_length=120)
    event_id = models.CharField(max_length=160, unique=True)
    payload = models.JSONField(default=dict, blank=True)
    status = models.CharField(max_length=32, default="pending")
    processed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.provider} - {self.event_type}"


class SyncJob(TimeStampedModel):
    connected_account = models.ForeignKey(
        "connected_accounts.ConnectedAccount",
        on_delete=models.CASCADE,
        related_name="sync_jobs",
    )
    job_type = models.CharField(max_length=80)
    status = models.CharField(max_length=32, default="pending")
    requested_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    details = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ("-requested_at",)

    def __str__(self):
        return f"{self.connected_account} - {self.job_type}"

# Create your models here.
