from django.contrib import admin

from .models import ConnectedAccount, PlatformMedia, PlatformMetricsSnapshot, PlatformProfile, SyncJob, WebhookEvent


@admin.register(ConnectedAccount)
class ConnectedAccountAdmin(admin.ModelAdmin):
    list_display = ("user", "provider", "username", "status", "token_status", "last_synced_at")
    list_filter = ("provider", "status", "token_status")
    search_fields = ("user__email", "username", "provider_account_id")


@admin.register(PlatformProfile)
class PlatformProfileAdmin(admin.ModelAdmin):
    list_display = ("display_name", "source_type", "verification_state", "follower_count")
    list_filter = ("source_type", "verification_state")
    search_fields = ("display_name",)


@admin.register(PlatformMetricsSnapshot)
class PlatformMetricsSnapshotAdmin(admin.ModelAdmin):
    list_display = ("platform_profile", "captured_at", "follower_count", "total_reach", "verification_state")
    list_filter = ("verification_state", "source_type")


@admin.register(PlatformMedia)
class PlatformMediaAdmin(admin.ModelAdmin):
    list_display = ("title", "media_type", "section", "view_count", "verification_state")
    list_filter = ("media_type", "section", "verification_state")
    search_fields = ("title",)


@admin.register(WebhookEvent)
class WebhookEventAdmin(admin.ModelAdmin):
    list_display = ("provider", "event_type", "event_id", "status", "processed_at")
    list_filter = ("provider", "status")


@admin.register(SyncJob)
class SyncJobAdmin(admin.ModelAdmin):
    list_display = ("connected_account", "job_type", "status", "requested_at", "finished_at")
    list_filter = ("status", "job_type")

# Register your models here.
