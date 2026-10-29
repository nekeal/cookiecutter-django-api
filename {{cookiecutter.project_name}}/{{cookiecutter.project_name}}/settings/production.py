import sentry_sdk
from django.utils.csp import CSP
from sentry_sdk.integrations.django import DjangoIntegration

from . import env
from .base import *

DEBUG = False

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", ["*"])

sentry_sdk.init(
    dsn=env("SENTRY_DSN", ""),
    integrations=[DjangoIntegration()],
)

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# ------------- SECURITY -------------
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", True)
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", True)
CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", True)
SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", 0)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", False)
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", False)

SECURE_CSP_REPORT_ONLY = {
    "default-src": [CSP.SELF],
    "script-src": [CSP.SELF, CSP.NONCE],
    "style-src": [CSP.SELF],
    "img-src": [CSP.SELF, "data:"],
    "font-src": [CSP.SELF, "data:"],
    "object-src": [CSP.NONE],
    "base-uri": [CSP.SELF],
}

# ------------- LOGGING -------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console_info": {
            "level": "ERROR",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        }
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console_info"],
        }
    },
}

# ------------- DATABASES -------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", "postgres"),
        "USER": env("POSTGRES_USER", "postgres"),
        "PASSWORD": env("POSTGRES_PASSWORD", ""),
        "HOST": env("POSTGRES_HOST", "localhost"),
        "OPTIONS": {"pool": True},
        "CONN_HEALTH_CHECKS": True,
    }
}

# ------------- STORAGES -------------
STORAGES = {
    **STORAGES,
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"},
}

# ------------- STATIC -------------
STATIC_ROOT = BASE_DIR.parent.joinpath("public")
MEDIA_ROOT = BASE_DIR.parent.joinpath("media")
