from django.contrib import admin

from .models import AuditEvent, ModerationFlag


@admin.register(AuditEvent)
class AuditEventAdmin(admin.ModelAdmin):
    list_display = ("action", "role_context", "target_type", "target_id", "created_at")
    list_filter = ("role_context", "action")
    search_fields = ("action", "target_type", "target_id")


@admin.register(ModerationFlag)
class ModerationFlagAdmin(admin.ModelAdmin):
    list_display = ("target_type", "target_id", "reason", "is_resolved", "created_at")
    list_filter = ("is_resolved",)
    search_fields = ("target_type", "target_id", "reason")

# Register your models here.
