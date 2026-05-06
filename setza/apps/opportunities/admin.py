from django.contrib import admin

from .models import Opportunity


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ("title", "brand_profile", "budget_min", "budget_max", "event_date", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "brand_profile__profile__display_name")

# Register your models here.
