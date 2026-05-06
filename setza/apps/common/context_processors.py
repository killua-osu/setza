from django.conf import settings


def global_ui(request):
    return {
        "setza_app_name": settings.SETZA_APP_NAME,
    }
