from django.db import models
from django.utils.text import slugify

from apps.common.models import TimeStampedModel


class Service(TimeStampedModel):
    creator_profile = models.ForeignKey(
        "accounts.CreatorProfile",
        on_delete=models.CASCADE,
        related_name="services",
    )
    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.CharField(max_length=220, blank=True)
    description = models.TextField(blank=True)
    price_from = models.PositiveIntegerField(default=0)
    turnaround_days = models.PositiveIntegerField(default=0)
    concepts = models.PositiveIntegerField(default=0)
    revisions = models.PositiveIntegerField(default=0)
    platforms = models.JSONField(default=list, blank=True)
    deliverables = models.JSONField(default=list, blank=True)
    location = models.CharField(max_length=120, blank=True)
    media_theme = models.CharField(max_length=80, default="theme-media-lifestyle-1")
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
