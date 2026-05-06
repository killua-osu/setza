from copy import deepcopy


def _gallery(*themes):
    counts = ["125K", "240K", "25K", "25K"]
    return [{"theme": theme, "views": counts[index]} for index, theme in enumerate(themes)]


def _service(slug, title, price, summary, turnaround, concepts, revisions, platforms, theme, inquiries, budget):
    return {
        "slug": slug,
        "title": title,
        "price": price,
        "summary": summary,
        "description": summary,
        "turnaround": turnaround,
        "concepts": concepts,
        "revisions": revisions,
        "platforms": platforms,
        "deliverables": ["1 Instagram Reel", "3 Instagram Stories"],
        "image_theme": theme,
        "inquiries": inquiries,
        "date": "16 March, 2026",
        "budget": budget,
        "location": "Nagpur, India",
    }


def _creator(slug, name, niche, avatar_theme, banner_theme, gallery_themes, platforms=None):
    return {
        "slug": slug,
        "name": name,
        "location": "Nagpur, India",
        "platforms": platforms or ["Instagram", "Facebook", "TikTok"],
        "niche": niche,
        "description": "A creator with premium, culture-led content and polished brand-friendly storytelling.",
        "followers": "125K",
        "reach": "259K",
        "engagement": "4.8%",
        "avatar_theme": avatar_theme,
        "banner_theme": banner_theme,
        "deliverables": ["3 TikTok Video", "1 TikTok Post", "1 Instagram Reel", "3 Instagram Stories", "1 Static Post"],
        "gallery": _gallery(*gallery_themes),
    }


def _brand(slug, banner_theme, gallery_themes):
    return {
        "slug": slug,
        "name": "Velour Collective",
        "location": "Nagpur, India",
        "platforms": ["Instagram", "Facebook", "TikTok", "Youtube"],
        "niche": "Nightlife & Experiential Events",
        "description": "Velour Collective creates premium, high-energy nightlife experiences across fashion and culture circles.",
        "avatar_theme": "theme-avatar-velour",
        "banner_theme": banner_theme,
        "campaign_engage": "4.8%",
        "campaign_frequency": "2-5",
        "event_footfall": "800-1500",
        "focus_tags": ["Urban Nightlife Culture", "Music-Led Exp", "Premium Club Events", "Immersive Social Atmosphere"],
        "gallery": _gallery(*gallery_themes),
    }


DISCOVER_FILTERS = {
    "left_top": [{"label": "Trending", "value": "trending"}, {"label": "Campaign", "value": "campaign"}],
    "role_options": [{"label": "Creators", "value": "creators"}, {"label": "Brands", "value": "brands"}],
    "categories": [
        {"title": "Lifestyle", "items": ["Luxury", "Parties / Nightlife", "Travel", "Fitness", "Daily Vlogs", "Cars / Bikes"]},
        {"title": "Fashion & Beauty", "items": ["Streetwear", "High Fashion", "Makeup", "Skincare", "Grooming", "Cars / Bikes"]},
        {"title": "Business", "items": ["Entrepreneurship", "Startups", "Marketing", "Personal Branding"]},
        {"title": "Regional / Cultural", "items": ["Hindi Content", "Marathi Content", "Punjabi Content"]},
    ],
    "search_filters": [
        {"label": "Countries", "name": "country", "options": ["India", "UAE", "UK"]},
        {"label": "Platform", "name": "platform", "options": ["Instagram", "Facebook", "TikTok", "YouTube"]},
        {"label": "Followers", "name": "followers", "options": ["30K+", "50K+", "100K+"]},
        {"label": "Format", "name": "format", "options": ["Reels", "Stories", "Static Posts", "YouTube Videos"]},
        {"label": "Engagement Rate", "name": "engagement", "options": ["3%+", "4%+", "5%+"]},
        {"label": "Gender", "name": "gender", "options": ["Female", "Male", "Any"]},
    ],
}


SERVICES = [
    _service("reel-production", "Reel Production", "From ₹3000", "High-energy reel concepts tailored for nightlife brands and event campaigns.", "10 Days", "3 Concepts", "2 Revision", ["Instagram", "Facebook"], "theme-media-service-1", 2, "3K onwards"),
    _service("short-form-video-creation", "Short-Form Video Creation", "From ₹5000", "Fast-moving edits designed for launches, event announcements, and brand-first content.", "15 Days", "2 Concepts", "3 Revision", ["YouTube", "Facebook"], "theme-media-service-2", 4, "5K onwards"),
    _service("brand-focused-content", "Brand-Focused Content", "From ₹3000", "Brand-safe, editorial content that keeps product and event messaging centered.", "10 Days", "3 Concepts", "2 Revision", ["Instagram", "Facebook", "YouTube", "TikTok"], "theme-media-service-3", 3, "3K onwards"),
    _service("influencer-campaign-content", "Influencer Campaign Content", "From ₹5000", "Campaign-aligned deliverables that help brands keep message consistency across content drops.", "10 Days", "2 Concepts", "2 Revision", ["Instagram", "TikTok"], "theme-media-service-4", 1, "5K onwards"),
    _service("influencer-campaign-content-variation", "Influencer Campaign Content", "From ₹5000", "A second campaign card variation matching the screenshot layout and density.", "3 Days", "3 Concepts", "2 Revision", ["Instagram", "Facebook"], "theme-media-service-5", 2, "5K onwards"),
]


DISCOVER_CREATORS = [
    _creator("ronald-richards", "Ronald Richards", "Lifestyle & Wellness", "theme-avatar-ronald", "theme-banner-lifestyle-1", ("theme-media-lifestyle-1", "theme-media-lifestyle-2", "theme-media-lifestyle-3")),
    _creator("kianna-korsgaard", "Kianna Korsgaard", "Food", "theme-avatar-kianna", "theme-banner-food-1", ("theme-media-food-1", "theme-media-food-2", "theme-media-food-3"), ["Instagram", "TikTok", "Youtube"]),
    _creator("maria-calzoni", "Maria Calzoni", "Fitness", "theme-avatar-maria", "theme-banner-fitness-1", ("theme-media-fitness-1", "theme-media-fitness-2", "theme-media-fitness-3")),
    _creator("martin-calzoni", "Martin Calzoni", "Business", "theme-avatar-martin", "theme-banner-business-1", ("theme-media-business-1", "theme-media-business-2", "theme-media-business-3")),
    _creator("skylar-herwitz", "Skylar Herwitz", "Travel", "theme-avatar-skylar", "theme-banner-travel-1", ("theme-media-travel-1", "theme-media-travel-2", "theme-media-travel-3")),
    _creator("gustavo-rosser", "Gustavo Rosser", "Art", "theme-avatar-gustavo", "theme-banner-art-1", ("theme-media-art-1", "theme-media-art-2", "theme-media-art-3")),
]


DISCOVER_BRANDS = [
    _brand("velour-collective", "theme-banner-brand-1", ("theme-media-nightlife-1", "theme-media-nightlife-2", "theme-media-nightlife-3")),
    _brand("velour-collective-b", "theme-banner-brand-2", ("theme-media-nightlife-4", "theme-media-nightlife-5", "theme-media-nightlife-6")),
    _brand("velour-collective-c", "theme-banner-brand-3", ("theme-media-nightlife-7", "theme-media-nightlife-8", "theme-media-nightlife-9")),
]


RONALD_PROFILE = {
    "slug": "ronald-richards",
    "name": "Ronald Richards",
    "hero_theme": "theme-hero-party",
    "avatar_theme": "theme-avatar-ronald",
    "role": "Creator",
    "category": "Lifestyle & Wellness",
    "description": "A lifestyle creator and nightlife-forward visual storyteller who connects brands with culture-driven audiences.",
    "location": "Nagpur, India",
    "gender": "Female",
    "age": "18-20",
    "status_tags": ["Available Now", "Open For Campaign", "Open For Collaboration"],
    "traits": ["Trendsetter", "Curator", "Storyteller", "Connector"],
    "audience_types": ["Urban", "Social", "Night-Focused"],
    "about": "Ronald Richards is a lifestyle-focused creator known for nightlife, fashion, and culturally tuned short-form storytelling. Her content blends premium event visuals with an approachable voice that helps campaign moments feel aspirational but real.",
    "pricing_range": "₹25,000 - 50,000",
    "contact_email": "ronald@setza.com",
    "partner_heading": "Previous partnership ad and branded content partners",
    "partner_copy": "Brands that the creator has worked with in the past year",
    "partnered_with": "Partnered with MYNTRA, SAADA and 4+ more",
    "hire_options": ["One Time", "Full Campaign"],
    "services": deepcopy(SERVICES),
    "analytics": {
        "platform_tabs": ["Instagram", "Facebook", "TikTok", "YouTube"],
        "overview_metrics": [
            {"value": "125K", "label": "Followers"},
            {"value": "259K", "label": "Total Reach"},
            {"value": "4.8%", "label": "Engagement"},
            {"value": "50K", "label": "Account Engage"},
            {"value": "30.5%", "label": "Hookrate"},
        ],
        "platform_cards": [
            {"name": "Instagram", "followers": "125K followers", "trust": "Verified via connected platform", "last_synced": "18 min ago"},
            {"name": "Facebook", "followers": "187K followers", "trust": "Manual data", "last_synced": "Last synced 2 days ago"},
            {"name": "TikTok", "followers": "254K followers", "trust": "Verified via connected platform", "last_synced": "11 min ago"},
            {"name": "Youtube", "followers": "45K followers", "trust": "Reconnect required", "last_synced": "Token expired"},
        ],
        "format_chips": ["Reels", "Stories", "Static Posts", "Youtube Videos"],
        "galleries": [
            {"title": "Partnership Ads", "copy": "This creator partnered with advertiser to create ad. The below partnership ads have been active within last year.", "items": _gallery("theme-media-lifestyle-1", "theme-media-lifestyle-2", "theme-media-lifestyle-3", "theme-media-lifestyle-4")},
            {"title": "Branded Content", "copy": "This creator partnered with brands to create content. The below partnership content have been active within last year.", "items": _gallery("theme-media-party-1", "theme-media-party-2", "theme-media-party-3", "theme-media-party-4")},
            {"title": "Creator Content", "copy": "The below creator content that the creator have created.", "items": _gallery("theme-media-party-5", "theme-media-party-6", "theme-media-party-7", "theme-media-party-8")},
        ],
    },
}


VELOUR_PROFILE = {
    "slug": "velour-collective",
    "name": "Velour Collective",
    "hero_theme": "theme-hero-blue",
    "avatar_theme": "theme-avatar-velour",
    "role": "Brand",
    "categories": ["Nightlife", "Fashion"],
    "description": "A premium nightlife and experiential events brand curating high-energy club nights and exclusive urban party experiences across major cities.",
    "location": "Nagpur, India",
    "status_tags": ["Available Now", "Open For Campaign", "Open For Collaboration"],
    "traits": ["High-Energy Atmosphere", "Live Event Coverage", "Crowd Interaction", "Urban Social Scene"],
    "audience_types": ["Urban", "Social", "Night-Focused"],
    "about": "Velour Collective is a Mumbai-based nightlife brand known for curated weekend club events, themed party nights, and high-energy music experiences targeting urban premium audiences.",
    "pricing_range": "₹25,000 - 50,000",
    "contact_email": "asdfgg@asdas.com",
    "partner_heading": "Previous partnership ad and branded content partners",
    "partner_copy": "Creators that the brand has worked with in the past year",
    "partnered_with": "Partnered with Ronald, Rohan and 4+ more",
    "focus_tags": ["Urban Nightlife Culture", "Music-Led Exp", "Premium Club Events", "Immersive Social Atmosphere"],
    "hire_options": ["One Time", "Full Campaign"],
    "opportunities": [
        {
            "slug": "club-event-promotion-campaign",
            "title": "Club Event Promotion Campaign",
            "brand": "Velour Collective",
            "budget": "₹60K–1.2L",
            "followers_target": "30K–150K",
            "engagement_requirement": "3%+ Engagement",
            "date": "16 March, 2026",
            "platforms": ["Instagram", "Facebook", "TikTok"],
            "overview": "Promoting an exclusive weekend club event targeting urban nightlife audiences through high-energy reels, story coverage, and live event engagement.",
            "deliverables": ["3 TikTok Video", "1 TikTok Post", "1 Instagram Reel", "3 Instagram Stories", "1 Static Post"],
            "location": "Nagpur, India",
            "thumbnail_theme": "theme-media-brand-thumb",
            "applicants": 2,
        }
    ],
    "analytics": {
        "overview_metrics": [
            {"value": "4%", "label": "Avg. Campaign Engage"},
            {"value": "2-3", "label": "Campaign Frequency"},
            {"value": "30+", "label": "Creator Partnered"},
            {"value": "60%", "label": "Repeated Creators"},
            {"value": "800-1500", "label": "Avg. Event Footfall"},
        ],
        "platform_cards": [
            {"name": "Instagram", "followers": "125K followers", "trust": "Verified via connected platform", "last_synced": "14 min ago"},
            {"name": "Facebook", "followers": "187K followers", "trust": "Manual data", "last_synced": "Last synced 3 days ago"},
            {"name": "TikTok", "followers": "254K followers", "trust": "Unavailable", "last_synced": "Not connected"},
            {"name": "Youtube", "followers": "45K followers", "trust": "Verified via connected platform", "last_synced": "42 min ago"},
        ],
        "format_chips": ["Reels", "Stories", "Static Posts", "Youtube Videos"],
        "galleries": [
            {"title": "Partnership Ads", "copy": "This creator partnered with advertiser to create ad. The below partnership ads have been active within last year.", "items": _gallery("theme-media-nightlife-1", "theme-media-nightlife-2", "theme-media-nightlife-3", "theme-media-nightlife-4")},
            {"title": "Branded Content", "copy": "The creator partnered with brands to create content. The below partnership content have been active within last year.", "items": _gallery("theme-media-nightlife-5", "theme-media-nightlife-6", "theme-media-nightlife-7", "theme-media-nightlife-8")},
            {"title": "Creator Content", "copy": "The below creator content that the creator have created.", "items": _gallery("theme-media-nightlife-9", "theme-media-nightlife-10", "theme-media-nightlife-11", "theme-media-nightlife-12")},
        ],
    },
}


PUBLIC_OPPORTUNITIES = [deepcopy(VELOUR_PROFILE["opportunities"][0]) for _ in range(3)]
PUBLIC_OPPORTUNITIES[1]["slug"] = "club-event-promotion-campaign-a"
PUBLIC_OPPORTUNITIES[2]["slug"] = "club-event-promotion-campaign-b"


SERVICE_APPLICATIONS = [
    {"slug": "velour-collective", "name": "Velour Collective", "role": "Brand", "avatar_theme": "theme-avatar-velour", "platforms": ["Instagram", "Facebook", "TikTok"], "followers": "125K Followers", "engagement": "4.8 Camp Engage", "reach": "259k Reach", "message": "We need dynamic reel content that translates the crowd energy and visual intensity of our club night into scroll-stopping social content", "status": "Pending"},
    {"slug": "violet-reds", "name": "Violet Reds", "role": "Creator", "avatar_theme": "theme-avatar-violet", "platforms": ["Instagram", "Facebook", "TikTok"], "followers": "95K Followers", "engagement": "3.7 Engagement", "reach": "175k Reach", "message": "I'm looking for a high-energy reel that captures the atmosphere and aesthetic of my nightlife content.", "status": "Pending"},
]


OPPORTUNITY_APPLICATIONS = [
    {"slug": "ronald-richards", "name": "Ronald Richards", "role": "Creator", "avatar_theme": "theme-avatar-ronald", "platforms": ["Instagram", "Facebook", "TikTok"], "followers": "125K Followers", "engagement": "4.8 Engagement", "reach": "259k Reach", "message": "I create high-energy nightlife content that captures atmosphere and audience emotion, and I'd love to bring that energy to your upcoming event.", "status": "Pending"},
    {"slug": "violet-reds", "name": "Violet Reds", "role": "Creator", "avatar_theme": "theme-avatar-violet", "platforms": ["Instagram", "Facebook", "TikTok"], "followers": "95K Followers", "engagement": "3.7 Engagement", "reach": "175k Reach", "message": "My content focuses on capturing the vibe, crowd energy, and cultural pulse of nightlife experiences, perfectly aligned with your event concept.", "status": "Pending"},
]


def _conversation(slug, name, avatar, meta, metric, context, preview, date, messages, type_label):
    return {"slug": slug, "name": name, "avatar_theme": avatar, "meta": meta, "metric": metric, "context": context, "preview": preview, "date": date, "messages": messages, "type": type_label}


MESSAGES = {
    "creator": {
        "tabs": ["All", "Services", "Collaboration"],
        "conversations": [
            _conversation("violet-reds", "Violet Reds", "theme-avatar-violet", "95K Followers", "3.7 Engagement", "Service : Reel Production", "Opportunity : Club Event Promotion Campaign", "3 Mar", [{"sender": "them", "time": "Fri 11:11 AM", "body": "My content focuses on capturing the vibe, crowd energy, and cultural pulse of nightlife experiences, perfectly aligned with your event concept."}, {"sender": "me", "time": "Fri 11:57 AM", "body": "That sounds like a perfect fit. I'd love to collaborate and bring the energy of your event to life through my lens. Let's move forward and create something impactful."}], "Creator"),
            _conversation("velour-collective", "Velour Collective", "theme-avatar-velour", "Brand", "", "Collab : Campaign", "Collab : Campaign", "4 Mar", [{"sender": "them", "time": "Thu 03:16 PM", "body": "We'd love to explore a reel-first package for our next weekend event and creator drop."}], "Brand"),
            _conversation("ronald-richards", "Ronald Richards", "theme-avatar-ronald", "Creator", "", "Collab : One-Time", "Collab : One-Time", "5 Mar", [{"sender": "them", "time": "Thu 08:00 PM", "body": "Sharing ideas for the next one-time collaboration slot."}], "Creator"),
        ],
    },
    "brand": {
        "tabs": ["All", "Opportunities", "Collaboration"],
        "conversations": [
            _conversation("violet-reds", "Violet Reds", "theme-avatar-violet", "95K Followers", "3.7 Engagement", "Opportunity : Club Event Promotion Campaign", "Opportunity : Club Event Promotion Campaign", "3 Mar", [{"sender": "them", "time": "Fri 11:11 AM", "body": "My content focuses on capturing the vibe, crowd energy, and cultural pulse of nightlife experiences, perfectly aligned with your event concept."}, {"sender": "me", "time": "Fri 11:57 AM", "body": "That sounds like a perfect fit. I'd love to collaborate and bring the energy of your event to life through my lens. Let's move forward and create something impactful."}], "Creator"),
            _conversation("velour-collective", "Velour Collective", "theme-avatar-velour", "Brand", "", "Collab : Campaign", "Collab : Campaign", "4 Mar", [{"sender": "me", "time": "Thu 03:16 PM", "body": "Sharing event plan details and the revised collaboration brief."}], "Brand"),
            _conversation("ronald-richards", "Ronald Richards", "theme-avatar-ronald", "Creator", "", "Collab : One-Time", "Collab : One-Time", "5 Mar", [{"sender": "them", "time": "Thu 08:00 PM", "body": "I can send a refined content sequence for the opening teaser."}], "Creator"),
        ],
    },
}


DASHBOARDS = {
    "creator": {
        "title": "Creator Dashboard",
        "subtitle": "Monitor your active engagements and pending actions.",
        "stats": [{"label": "Active Service", "value": 4, "icon": "gift"}, {"label": "Pending Actions", "value": 7, "icon": "hourglass"}, {"label": "Active Conversations", "value": 2, "icon": "message-circle"}],
        "actions_required": [{"title": "Inquiries", "value": "2 New Applicants", "copy": "Across 1 Service", "action": "Review Inquiries", "icon": "badge-check"}, {"title": "Proposals", "value": "2 New Proposal Awaiting Response", "copy": "Review Proposals", "action": "Review Proposals", "icon": "file-check-2"}, {"title": "Messages", "value": "3 Unread Messages", "copy": "New messages from creators and brands", "action": "Open Inbox", "icon": "lock-keyhole-open"}],
        "quick_actions": [{"title": "Create Opportunity", "copy": "Launch a new campaign and start receiving applications", "icon": "plus"}, {"title": "Discover Partners", "copy": "Search and connect with aligned creators and brands", "icon": "users"}, {"title": "Edit Profile", "copy": "Update your profile information and service details", "icon": "square-pen"}],
    },
    "brand": {
        "title": "Brand Dashboard",
        "subtitle": "Monitor your active engagements and pending actions.",
        "stats": [{"label": "Active Service", "value": 4, "icon": "gift"}, {"label": "Pending Actions", "value": 7, "icon": "hourglass"}, {"label": "Active Conversations", "value": 2, "icon": "message-circle"}],
        "actions_required": [{"title": "Inquiries", "value": "2 New Applicants", "copy": "Across 1 Service", "action": "Review Inquiries", "icon": "badge-check"}, {"title": "Proposals", "value": "2 New Proposal Awaiting Response", "copy": "Review Proposals", "action": "Review Proposals", "icon": "file-check-2"}, {"title": "Messages", "value": "3 Unread Messages", "copy": "New messages from creators and brands", "action": "Open Inbox", "icon": "lock-keyhole-open"}],
        "quick_actions": [{"title": "Create Opportunity", "copy": "Launch a new campaign and start receiving applications", "icon": "plus"}, {"title": "Discover Partners", "copy": "Search and connect with aligned creators and brands", "icon": "users"}, {"title": "Edit Profile", "copy": "Update your brand's profile and information.", "icon": "square-pen"}],
    },
}


CONNECTED_ACCOUNTS = [
    {"provider": "Instagram", "status": "connected", "username": "@ronaldrichards", "profile_image_theme": "theme-avatar-ronald", "scopes": ["basic_profile", "insights", "media_list"], "last_synced": "18 minutes ago", "token_state": "Active", "copy": "Connect Instagram to unlock verified analytics"},
    {"provider": "TikTok", "status": "syncing", "username": "@ronald.reels", "profile_image_theme": "theme-avatar-violet", "scopes": ["video_metrics", "profile_read"], "last_synced": "Syncing now", "token_state": "Active", "copy": "Connect TikTok to import short-form performance metrics"},
    {"provider": "YouTube", "status": "reconnect_required", "username": "@ronaldstories", "profile_image_theme": "theme-avatar-kianna", "scopes": ["channel_read", "analytics_read"], "last_synced": "3 days ago", "token_state": "Expired", "copy": "Connect YouTube to display channel insights"},
]


def _clone(value):
    return deepcopy(value)


def get_discover_cards(kind="creators"): return _clone(DISCOVER_CREATORS if kind == "creators" else DISCOVER_BRANDS)


def get_public_opportunities(): return _clone(PUBLIC_OPPORTUNITIES)


def get_creator_profile(slug="ronald-richards"): return _clone(RONALD_PROFILE)


def get_brand_profile(slug="velour-collective"): return _clone(VELOUR_PROFILE)


def get_dashboard(role="creator"): return _clone(DASHBOARDS[role])


def get_messages(role="creator"): return _clone(MESSAGES[role])


def get_services(): return _clone(SERVICES)


def get_service(slug="reel-production"):
    return next((_clone(item) for item in SERVICES if item["slug"] == slug), _clone(SERVICES[0]))


def get_service_applications(): return _clone(SERVICE_APPLICATIONS)


def get_brand_opportunities(): return _clone(VELOUR_PROFILE["opportunities"] * 3)


def get_opportunity(slug="club-event-promotion-campaign"):
    return next((_clone(item) for item in PUBLIC_OPPORTUNITIES if item["slug"] == slug), _clone(PUBLIC_OPPORTUNITIES[0]))


def get_opportunity_applications(): return _clone(OPPORTUNITY_APPLICATIONS)


def get_collaborations(role="creator"):
    return {"summary": [{"label": "One-Time", "value": 2, "icon": "users-round"}, {"label": "Campaign", "value": 4, "icon": "briefcase-business"}], "tabs": ["One-Time", "Campaign"], "items": get_service_applications() if role == "creator" else get_opportunity_applications()}


def get_connected_accounts(): return _clone(CONNECTED_ACCOUNTS)
