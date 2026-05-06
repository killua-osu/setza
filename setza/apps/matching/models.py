from django.db import models

from apps.common.models import TimeStampedModel


class MatchScore(TimeStampedModel):
    creator_profile = models.ForeignKey(
        "accounts.CreatorProfile",
        on_delete=models.CASCADE,
        related_name="match_scores",
    )
    brand_profile = models.ForeignKey(
        "accounts.BrandProfile",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="match_scores",
    )
    opportunity = models.ForeignKey(
        "opportunities.Opportunity",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="match_scores",
    )
    service = models.ForeignKey(
        "services.Service",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="match_scores",
    )
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    summary = models.CharField(max_length=255, blank=True)
    breakdown = models.JSONField(default=dict, blank=True)
    is_current = models.BooleanField(default=True)

    class Meta:
        ordering = ("-score", "-updated_at")

    def __str__(self):
        return f"{self.creator_profile.profile.display_name} - {self.score}"

# Create your models here.
