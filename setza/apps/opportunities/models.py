from django.db import models
from django.utils.text import slugify

from apps.common.models import TimeStampedModel


class Opportunity(TimeStampedModel):
    brand_profile = models.ForeignKey(
        "accounts.BrandProfile",
        on_delete=models.CASCADE,
        related_name="opportunities",
    )
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True, blank=True)
    description = models.CharField(max_length=240, blank=True)
    overview = models.TextField(blank=True)
    budget_min = models.PositiveIntegerField(default=0)
    budget_max = models.PositiveIntegerField(default=0)
    follower_min = models.PositiveIntegerField(default=0)
    follower_max = models.PositiveIntegerField(default=0)
    engagement_requirement = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    platforms = models.JSONField(default=list, blank=True)
    deliverables = models.JSONField(default=list, blank=True)
    event_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=120, blank=True)
    media_theme = models.CharField(max_length=80, default="theme-media-nightlife-1")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("title",)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Create your models here.
