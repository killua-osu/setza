from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.text import slugify

from apps.common.choices import RoleType
from apps.common.models import TimeStampedModel


class SetzaUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email address is required.")
        email = self.normalize_email(email)
        username = extra_fields.get("username") or email.split("@")[0]
        extra_fields["username"] = username
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    active_role = models.CharField(max_length=20, choices=RoleType.choices, default=RoleType.CREATOR)
    is_onboarded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = SetzaUserManager()

    def __str__(self):
        return self.email


class Role(TimeStampedModel):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="roles")
    role = models.CharField(max_length=20, choices=RoleType.choices)
    is_primary = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "role")
        ordering = ("user", "role")

    def __str__(self):
        return f"{self.user.email} - {self.role}"


class Profile(TimeStampedModel):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE, related_name="profile")
    display_name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    primary_role = models.CharField(max_length=20, choices=RoleType.choices, default=RoleType.CREATOR)
    headline = models.CharField(max_length=180, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    banner_theme = models.CharField(max_length=80, default="theme-hero-night")
    avatar_theme = models.CharField(max_length=80, default="theme-avatar-rose")
    pricing_range = models.CharField(max_length=80, blank=True)
    contact_email = models.EmailField(blank=True)
    audience_types = models.JSONField(default=list, blank=True)
    traits = models.JSONField(default=list, blank=True)
    status_tags = models.JSONField(default=list, blank=True)
    deliverables = models.JSONField(default=list, blank=True)
    languages = models.JSONField(default=list, blank=True)

    class Meta:
        ordering = ("display_name",)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.display_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.display_name


class CreatorProfile(TimeStampedModel):
    profile = models.OneToOneField("accounts.Profile", on_delete=models.CASCADE, related_name="creator_profile")
    gender = models.CharField(max_length=32, blank=True)
    age_range = models.CharField(max_length=32, blank=True)
    niches = models.JSONField(default=list, blank=True)
    follower_count = models.PositiveIntegerField(default=0)
    reach_count = models.PositiveIntegerField(default=0)
    engagement_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    hook_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    account_engaged = models.PositiveIntegerField(default=0)
    match_keywords = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"Creator: {self.profile.display_name}"


class BrandProfile(TimeStampedModel):
    profile = models.OneToOneField("accounts.Profile", on_delete=models.CASCADE, related_name="brand_profile")
    categories = models.JSONField(default=list, blank=True)
    focus_tags = models.JSONField(default=list, blank=True)
    avg_campaign_engagement = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    campaign_frequency = models.CharField(max_length=32, blank=True)
    repeated_creators_rate = models.CharField(max_length=32, blank=True)
    avg_event_footfall = models.CharField(max_length=32, blank=True)
    creator_partners_count = models.PositiveIntegerField(default=0)
    match_keywords = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"Brand: {self.profile.display_name}"

# Create your models here.
