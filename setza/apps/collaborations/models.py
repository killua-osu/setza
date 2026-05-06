from django.db import models

from apps.common.choices import ApplicationStatus, CollaborationType, RoleType
from apps.common.models import TimeStampedModel


class Application(TimeStampedModel):
    applicant_profile = models.ForeignKey(
        "accounts.Profile",
        on_delete=models.CASCADE,
        related_name="applications",
    )
    applicant_role = models.CharField(max_length=20, choices=RoleType.choices)
    service = models.ForeignKey(
        "services.Service",
        on_delete=models.CASCADE,
        related_name="applications",
        null=True,
        blank=True,
    )
    opportunity = models.ForeignKey(
        "opportunities.Opportunity",
        on_delete=models.CASCADE,
        related_name="applications",
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=20, choices=ApplicationStatus.choices, default=ApplicationStatus.PENDING)
    message = models.TextField()
    follower_count = models.PositiveIntegerField(default=0)
    reach_count = models.PositiveIntegerField(default=0)
    engagement_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    match_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    review_notes = models.TextField(blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.applicant_profile.display_name} ({self.status})"


class Collaboration(TimeStampedModel):
    creator_profile = models.ForeignKey(
        "accounts.CreatorProfile",
        on_delete=models.CASCADE,
        related_name="collaborations",
    )
    brand_profile = models.ForeignKey(
        "accounts.BrandProfile",
        on_delete=models.CASCADE,
        related_name="collaborations",
    )
    application = models.ForeignKey(
        "collaborations.Application",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="collaborations",
    )
    collaboration_type = models.CharField(max_length=20, choices=CollaborationType.choices)
    status = models.CharField(max_length=32, default="pending")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    value_min = models.PositiveIntegerField(default=0)
    value_max = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.brand_profile.profile.display_name} x {self.creator_profile.profile.display_name}"

# Create your models here.
