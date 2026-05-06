from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.accounts.models import BrandProfile, CreatorProfile, Profile, Role, User
from apps.collaborations.models import Application, Collaboration
from apps.common.choices import (
    ApplicationStatus,
    CollaborationType,
    ConnectionStatus,
    ConversationType,
    DataSourceType,
    PlatformType,
    RoleType,
    TokenStatus,
    VerificationState,
)
from apps.common.mock_data import RONALD_PROFILE, SERVICES, SERVICE_APPLICATIONS, VELOUR_PROFILE
from apps.common.models import AuditEvent
from apps.connected_accounts.models import ConnectedAccount, PlatformMedia, PlatformMetricsSnapshot, PlatformProfile
from apps.matching.models import MatchScore
from apps.messaging.models import Conversation, Message
from apps.notifications.models import Notification
from apps.opportunities.models import Opportunity
from apps.services.models import Service


class Command(BaseCommand):
    help = "Seed Setza demo content"

    def handle(self, *args, **options):
        creator_user, _ = User.objects.get_or_create(
            email="creator@setza.com",
            defaults={"username": "creator", "active_role": RoleType.CREATOR, "is_onboarded": True},
        )
        creator_user.set_password("demo1234")
        creator_user.save()

        brand_user, _ = User.objects.get_or_create(
            email="brand@setza.com",
            defaults={"username": "brand", "active_role": RoleType.BRAND, "is_onboarded": True},
        )
        brand_user.set_password("demo1234")
        brand_user.save()

        Role.objects.get_or_create(user=creator_user, role=RoleType.CREATOR, defaults={"is_primary": True})
        Role.objects.get_or_create(user=brand_user, role=RoleType.BRAND, defaults={"is_primary": True})

        creator_profile, _ = Profile.objects.update_or_create(
            user=creator_user,
            defaults={
                "display_name": RONALD_PROFILE["name"],
                "primary_role": RoleType.CREATOR,
                "headline": RONALD_PROFILE["category"],
                "bio": RONALD_PROFILE["description"],
                "location": RONALD_PROFILE["location"],
                "banner_theme": RONALD_PROFILE["hero_theme"],
                "avatar_theme": RONALD_PROFILE["avatar_theme"],
                "pricing_range": RONALD_PROFILE["pricing_range"],
                "contact_email": RONALD_PROFILE["contact_email"],
                "audience_types": RONALD_PROFILE["audience_types"],
                "traits": RONALD_PROFILE["traits"],
                "status_tags": RONALD_PROFILE["status_tags"],
                "deliverables": SERVICES[0]["deliverables"],
            },
        )
        creator_detail, _ = CreatorProfile.objects.update_or_create(
            profile=creator_profile,
            defaults={
                "gender": RONALD_PROFILE["gender"],
                "age_range": RONALD_PROFILE["age"],
                "niches": [RONALD_PROFILE["category"]],
                "follower_count": 125000,
                "reach_count": 259000,
                "engagement_rate": 4.8,
                "hook_rate": 30.5,
                "account_engaged": 50000,
                "match_keywords": ["nightlife", "lifestyle", "fashion"],
            },
        )

        brand_profile, _ = Profile.objects.update_or_create(
            user=brand_user,
            defaults={
                "display_name": VELOUR_PROFILE["name"],
                "primary_role": RoleType.BRAND,
                "headline": ", ".join(VELOUR_PROFILE["categories"]),
                "bio": VELOUR_PROFILE["description"],
                "location": VELOUR_PROFILE["location"],
                "banner_theme": VELOUR_PROFILE["hero_theme"],
                "avatar_theme": VELOUR_PROFILE["avatar_theme"],
                "pricing_range": VELOUR_PROFILE["pricing_range"],
                "contact_email": VELOUR_PROFILE["contact_email"],
                "audience_types": VELOUR_PROFILE["audience_types"],
                "traits": VELOUR_PROFILE["traits"],
                "status_tags": VELOUR_PROFILE["status_tags"],
                "deliverables": VELOUR_PROFILE["opportunities"][0]["deliverables"],
            },
        )
        brand_detail, _ = BrandProfile.objects.update_or_create(
            profile=brand_profile,
            defaults={
                "categories": VELOUR_PROFILE["categories"],
                "focus_tags": VELOUR_PROFILE["focus_tags"],
                "avg_campaign_engagement": 4,
                "campaign_frequency": "2-3",
                "repeated_creators_rate": "60%",
                "avg_event_footfall": "800-1500",
                "creator_partners_count": 30,
                "match_keywords": ["nightlife", "events", "fashion"],
            },
        )

        seeded_services = []
        for item in SERVICES[:3]:
            service, _ = Service.objects.update_or_create(
                slug=item["slug"],
                defaults={
                    "creator_profile": creator_detail,
                    "title": item["title"],
                    "summary": item["summary"],
                    "description": item["description"],
                    "price_from": int(item["budget"].split("K")[0]) * 1000,
                    "turnaround_days": int(item["turnaround"].split()[0]),
                    "concepts": int(item["concepts"].split()[0]),
                    "revisions": int(item["revisions"].split()[0]),
                    "platforms": item["platforms"],
                    "deliverables": item["deliverables"],
                    "location": item["location"],
                    "media_theme": item["image_theme"],
                },
            )
            seeded_services.append(service)

        opportunity_data = VELOUR_PROFILE["opportunities"][0]
        opportunity, _ = Opportunity.objects.update_or_create(
            slug=opportunity_data["slug"],
            defaults={
                "brand_profile": brand_detail,
                "title": opportunity_data["title"],
                "description": opportunity_data["overview"],
                "overview": opportunity_data["overview"],
                "budget_min": 60000,
                "budget_max": 120000,
                "follower_min": 30000,
                "follower_max": 150000,
                "engagement_requirement": 3,
                "platforms": opportunity_data["platforms"],
                "deliverables": opportunity_data["deliverables"],
                "event_date": date(2026, 3, 16),
                "location": opportunity_data["location"],
                "media_theme": opportunity_data["thumbnail_theme"],
            },
        )

        service_application, _ = Application.objects.update_or_create(
            applicant_profile=brand_profile,
            service=seeded_services[0],
            defaults={
                "applicant_role": RoleType.BRAND,
                "status": ApplicationStatus.PENDING,
                "message": SERVICE_APPLICATIONS[0]["message"],
                "follower_count": 125000,
                "reach_count": 259000,
                "engagement_rate": 4.8,
                "match_score": 86,
            },
        )

        opportunity_application, _ = Application.objects.update_or_create(
            applicant_profile=creator_profile,
            opportunity=opportunity,
            defaults={
                "applicant_role": RoleType.CREATOR,
                "status": ApplicationStatus.PENDING,
                "message": "I create high-energy nightlife content that captures atmosphere and audience emotion.",
                "follower_count": 125000,
                "reach_count": 259000,
                "engagement_rate": 4.8,
                "match_score": 91,
            },
        )

        collaboration, _ = Collaboration.objects.update_or_create(
            creator_profile=creator_detail,
            brand_profile=brand_detail,
            application=opportunity_application,
            defaults={
                "collaboration_type": CollaborationType.CAMPAIGN,
                "status": "pending",
                "start_date": date(2026, 3, 12),
                "end_date": date(2026, 3, 20),
                "value_min": 60000,
                "value_max": 120000,
                "notes": "Rule-based match approved for demo.",
            },
        )

        conversation, _ = Conversation.objects.update_or_create(
            creator_profile=creator_detail,
            brand_profile=brand_detail,
            topic_label=opportunity.title,
            defaults={
                "topic_type": ConversationType.OPPORTUNITY,
                "opportunity": opportunity,
                "collaboration": collaboration,
                "last_message_preview": "Let's move forward and create something impactful.",
                "last_message_at": timezone.now(),
                "unread_count_brand": 1,
            },
        )

        Message.objects.get_or_create(
            conversation=conversation,
            sender=creator_user,
            body="That sounds like a perfect fit. I'd love to collaborate and bring the energy of your event to life through my lens.",
        )

        Notification.objects.get_or_create(
            user=brand_user,
            title="New application received",
            defaults={"body": "Ronald Richards applied to Club Event Promotion Campaign.", "notification_type": "application"},
        )

        instagram, _ = ConnectedAccount.objects.update_or_create(
            user=creator_user,
            provider=PlatformType.INSTAGRAM,
            provider_account_id="ig_ronald_001",
            defaults={
                "username": "ronaldrichards",
                "status": ConnectionStatus.CONNECTED,
                "token_status": TokenStatus.ACTIVE,
                "connected_at": timezone.now() - timedelta(days=4),
                "last_synced_at": timezone.now() - timedelta(minutes=18),
            },
        )
        platform_profile, _ = PlatformProfile.objects.update_or_create(
            connected_account=instagram,
            defaults={
                "display_name": "Ronald Richards",
                "follower_count": 125000,
                "reach_count": 259000,
                "engagement_rate": 4.8,
                "source_type": DataSourceType.CONNECTED_PLATFORM,
                "verification_state": VerificationState.VERIFIED,
            },
        )
        PlatformMetricsSnapshot.objects.get_or_create(
            platform_profile=platform_profile,
            captured_at=timezone.now() - timedelta(hours=1),
            defaults={
                "follower_count": 125000,
                "total_reach": 259000,
                "engagement_rate": 4.8,
                "account_engaged": 50000,
                "hook_rate": 30.5,
                "verification_state": VerificationState.VERIFIED,
                "source_type": DataSourceType.CONNECTED_PLATFORM,
            },
        )
        PlatformMedia.objects.get_or_create(
            platform_profile=platform_profile,
            title="Nightlife Reel",
            defaults={
                "media_type": "reel",
                "section": "Branded Content",
                "thumbnail_theme": "theme-media-party-1",
                "view_count": 125000,
                "verification_state": VerificationState.VERIFIED,
                "source_type": DataSourceType.CONNECTED_PLATFORM,
            },
        )

        MatchScore.objects.get_or_create(
            creator_profile=creator_detail,
            brand_profile=brand_detail,
            opportunity=opportunity,
            defaults={
                "service": seeded_services[0],
                "score": 91,
                "summary": "Strong nightlife niche fit with audience and platform alignment.",
                "breakdown": {
                    "niche_fit": 20,
                    "platform_fit": 19,
                    "location_fit": 18,
                    "engagement_fit": 17,
                    "budget_fit": 17,
                    "availability_fit": 0,
                },
            },
        )

        AuditEvent.objects.get_or_create(
            actor=brand_user,
            action="seed_demo_data",
            target_type="opportunity",
            target_id=str(opportunity.id),
            defaults={"role_context": RoleType.BRAND, "metadata": {"source": "management_command"}},
        )

        self.stdout.write(self.style.SUCCESS("Setza demo data seeded."))
