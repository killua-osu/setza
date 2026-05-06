from django.contrib import admin

from .models import Application, Collaboration


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("applicant_profile", "applicant_role", "status", "match_score", "created_at")
    list_filter = ("applicant_role", "status")
    search_fields = ("applicant_profile__display_name",)


@admin.register(Collaboration)
class CollaborationAdmin(admin.ModelAdmin):
    list_display = ("creator_profile", "brand_profile", "collaboration_type", "status", "start_date")
    list_filter = ("collaboration_type", "status")

# Register your models here.
