{%- if cookiecutter.use_sentry == "y" %}
from sentry_sdk.integrations.django import DjangoIntegration
{%- endif %}
from .base import *

DEBUG = False

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", ["*"])

{%- if cookiecutter.use_sentry == "y" %}
sentry_sdk.init(
    dsn="",
    integrations=[DjangoIntegration()],
)
{%- endif %}

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
    }
}

# ------------- STATIC -------------
STATIC_ROOT = BASE_DIR.parent.joinpath("public")
MEDIA_ROOT = BASE_DIR.parent.joinpath("media")
