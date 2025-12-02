from . import env
from .base import *

SECRET_KEY = "secret_key"  # noqa: S105

# ------------- DATABASES -------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", "{{ cookiecutter.project_name }}"),
        "USER": env("POSTGRES_USER", "{{ cookiecutter.project_name }}"),
        "PASSWORD": env("POSTGRES_PASSWORD", "{{ cookiecutter.project_name }}"),
        "HOST": env("POSTGRES_HOST", "localhost"),
    }
}

# ------------- CSRF -------------
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]