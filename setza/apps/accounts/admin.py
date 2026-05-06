from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import BrandProfile, CreatorProfile, Profile, Role, User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ("email", "username", "active_role", "is_staff", "is_onboarded")
    ordering = ("email",)
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Setza", {"fields": ("active_role", "is_onboarded")}),
    )
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (
        ("Setza", {"fields": ("email", "active_role", "is_onboarded")}),
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "is_primary", "created_at")
    list_filter = ("role", "is_primary")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("display_name", "primary_role", "location", "contact_email")
    list_filter = ("primary_role",)
    search_fields = ("display_name", "location", "contact_email")


@admin.register(CreatorProfile)
class CreatorProfileAdmin(admin.ModelAdmin):
    list_display = ("profile", "gender", "age_range", "follower_count", "engagement_rate")
    search_fields = ("profile__display_name",)


@admin.register(BrandProfile)
class BrandProfileAdmin(admin.ModelAdmin):
    list_display = ("profile", "campaign_frequency", "creator_partners_count", "avg_event_footfall")
    search_fields = ("profile__display_name",)

# Register your models here.
