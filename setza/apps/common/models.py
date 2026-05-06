from django.conf import settings
from django.db import models

from .choices import RoleType


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuditEvent(TimeStampedModel):
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_events",
    )
    role_context = models.CharField(max_length=20, choices=RoleType.choices, default=RoleType.CREATOR)
    action = models.CharField(max_length=120)
    target_type = models.CharField(max_length=120, blank=True)
    target_id = models.CharField(max_length=64, blank=True)
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.action} ({self.role_context})"


class ModerationFlag(TimeStampedModel):
    target_type = models.CharField(max_length=120)
    target_id = models.CharField(max_length=64)
    reason = models.CharField(max_length=255)
    is_resolved = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.target_type}:{self.target_id}"
