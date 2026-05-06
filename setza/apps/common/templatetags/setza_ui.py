from django import template

register = template.Library()


@register.filter
def in_path(path, prefix):
    return path.startswith(prefix)


@register.filter
def compact_number(value):
    if value is None:
        return ""
    if value >= 1_000_000:
        return f"{value/1_000_000:.1f}M"
    if value >= 1_000:
        return f"{value/1_000:.0f}K"
    return str(value)


@register.filter
def percentage(value):
    return f"{value}%"


@register.filter
def get_item(mapping, key):
    if isinstance(mapping, dict):
        return mapping.get(key, "")
    return ""
