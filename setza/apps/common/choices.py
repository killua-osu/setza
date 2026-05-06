from django.db import models


class RoleType(models.TextChoices):
    CREATOR = "creator", "Creator"
    BRAND = "brand", "Brand"


class VerificationState(models.TextChoices):
    VERIFIED = "verified", "Verified"
    SELF_REPORTED = "self_reported", "Self Reported"
    EXPIRED = "expired", "Expired"
    UNAVAILABLE = "unavailable", "Unavailable"


class DataSourceType(models.TextChoices):
    CONNECTED_PLATFORM = "connected_platform", "Connected Platform"
    MANUAL = "manual", "Manual"
    IMPORTED = "imported", "Imported"


class ConnectionStatus(models.TextChoices):
    CONNECTED = "connected", "Connected"
    NOT_CONNECTED = "not_connected", "Not Connected"
    SYNCING = "syncing", "Syncing"
    EXPIRED = "expired", "Expired"
    RECONNECT_REQUIRED = "reconnect_required", "Reconnect Required"
    FAILED = "failed", "Failed"


class TokenStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    EXPIRING = "expiring", "Expiring"
    EXPIRED = "expired", "Expired"
    REVOKED = "revoked", "Revoked"


class PlatformType(models.TextChoices):
    INSTAGRAM = "instagram", "Instagram"
    FACEBOOK = "facebook", "Facebook"
    TIKTOK = "tiktok", "TikTok"
    YOUTUBE = "youtube", "YouTube"


class CollaborationType(models.TextChoices):
    ONE_TIME = "one_time", "One-Time"
    CAMPAIGN = "campaign", "Campaign"


class ApplicationStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    ACCEPTED = "accepted", "Accepted"
    REJECTED = "rejected", "Rejected"
    ARCHIVED = "archived", "Archived"


class ConversationType(models.TextChoices):
    SERVICE = "service", "Service"
    OPPORTUNITY = "opportunity", "Opportunity"
    COLLABORATION = "collaboration", "Collaboration"
