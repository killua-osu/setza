ROLE_SWITCH_MAP = {
    "creator:dashboard": {"creator": "creator:dashboard", "brand": "brand:dashboard"},
    "creator:messages": {"creator": "creator:messages", "brand": "brand:messages"},
    "creator:services": {"creator": "creator:services", "brand": "brand:opportunities"},
    "creator:service_detail": {"creator": "creator:service_detail", "brand": "brand:opportunity_detail"},
    "creator:collaborations": {"creator": "creator:collaborations", "brand": "brand:collaborations"},
    "creator:profile_services": {"creator": "creator:profile_services", "brand": "brand:profile_opportunities"},
    "creator:profile_analytics": {"creator": "creator:profile_analytics", "brand": "brand:profile_analytics"},
    "discover:creator_discover": {"creator": "discover:creator_discover", "brand": "discover:brand_discover"},
    "discover:creator_opportunities": {"creator": "discover:creator_opportunities", "brand": "discover:creator_opportunities"},
    "brand:dashboard": {"creator": "creator:dashboard", "brand": "brand:dashboard"},
    "brand:messages": {"creator": "creator:messages", "brand": "brand:messages"},
    "brand:opportunities": {"creator": "creator:services", "brand": "brand:opportunities"},
    "brand:opportunity_detail": {"creator": "creator:service_detail", "brand": "brand:opportunity_detail"},
    "brand:collaborations": {"creator": "creator:collaborations", "brand": "brand:collaborations"},
    "brand:profile_opportunities": {"creator": "creator:profile_services", "brand": "brand:profile_opportunities"},
    "brand:profile_analytics": {"creator": "creator:profile_analytics", "brand": "brand:profile_analytics"},
    "accounts:sign_in": {"creator": "accounts:sign_in", "brand": "accounts:sign_in"},
}


HEADER_ITEMS = [
    {"key": "dashboard", "label": "Dashboard"},
    {"key": "discover", "label": "Discover"},
    {"key": "opportunities", "label": "Opportunities"},
]


DASHBOARD_SIDEBARS = {
    "creator": [
        {"key": "overview", "label": "Overview", "route": "creator:dashboard"},
        {"key": "profile", "label": "Profile", "route": "creator:profile_services"},
        {"key": "messages", "label": "Messages", "route": "creator:messages"},
        {"key": "services", "label": "Services", "route": "creator:services"},
        {"key": "collaborations", "label": "Collaborations", "route": "creator:collaborations"},
    ],
    "brand": [
        {"key": "overview", "label": "Overview", "route": "brand:dashboard"},
        {"key": "profile", "label": "Profile", "route": "brand:profile_opportunities"},
        {"key": "messages", "label": "Messages", "route": "brand:messages"},
        {"key": "opportunities", "label": "Opportunities", "route": "brand:opportunities"},
        {"key": "collaborations", "label": "Collaborations", "route": "brand:collaborations"},
    ],
}
