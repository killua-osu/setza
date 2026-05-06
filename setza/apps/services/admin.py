from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "creator_profile", "price_from", "turnaround_days", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "creator_profile__profile__display_name")

# Register your models here.
