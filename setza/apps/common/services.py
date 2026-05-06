from django.urls import NoReverseMatch, reverse

from .navigation import DASHBOARD_SIDEBARS, HEADER_ITEMS, ROLE_SWITCH_MAP


def _header_routes(role):
    if role == "brand":
        return {
            "dashboard": "brand:dashboard",
            "discover": "discover:brand_discover",
            "opportunities": "brand:opportunities",
        }
    return {
        "dashboard": "creator:dashboard",
        "discover": "discover:creator_discover",
        "opportunities": "discover:creator_opportunities",
    }


def build_layout_context(request, role, active_nav, active_sidebar=None, switch_kwargs=None):
    switch_kwargs = switch_kwargs or {}
    view_name = request.resolver_match.view_name if request.resolver_match else ""
    switch_map = ROLE_SWITCH_MAP.get(view_name, {"creator": "creator:dashboard", "brand": "brand:dashboard"})
    header_items = []

    for item in HEADER_ITEMS:
        route_name = _header_routes(role)[item["key"]]
        header_items.append(
            {
                "key": item["key"],
                "label": item["label"],
                "url": reverse(route_name),
                "is_active": item["key"] == active_nav,
            }
        )

    sidebar = []
    for item in DASHBOARD_SIDEBARS.get(role, []):
        sidebar.append({**item, "url": reverse(item["route"]), "is_active": item["key"] == active_sidebar})

    role_switch = {}
    for role_name, route_name in switch_map.items():
        kwargs = switch_kwargs.get(role_name, {})
        try:
            role_switch[role_name] = reverse(route_name, kwargs=kwargs)
        except NoReverseMatch:
            role_switch[role_name] = reverse(f"{role_name}:dashboard")

    return {
        "current_role": role,
        "header_items": header_items,
        "dashboard_sidebar": sidebar,
        "role_switch": role_switch,
    }
