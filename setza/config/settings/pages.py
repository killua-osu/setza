import os

from .base import *  # noqa: F401,F403

DEBUG = False
SECRET_KEY = os.getenv("SECRET_KEY", "setza-github-pages-export-key")
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / ".pages.sqlite3",
    }
}

GITHUB_PAGES_BASE_PATH = os.getenv("GITHUB_PAGES_BASE_PATH", "").strip("/")
STATIC_URL = "/static/"
FORCE_SCRIPT_NAME = None

STATIC_ROOT = BASE_DIR / "dist" / "static"
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
