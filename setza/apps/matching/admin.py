from django.contrib import admin

from .models import MatchScore


@admin.register(MatchScore)
class MatchScoreAdmin(admin.ModelAdmin):
    list_display = ("creator_profile", "brand_profile", "opportunity", "service", "score", "is_current")
    list_filter = ("is_current",)

# Register your models here.
