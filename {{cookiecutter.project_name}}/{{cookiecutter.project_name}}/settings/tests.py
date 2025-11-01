from . import env
from .base import *

DEBUG = False
SECRET_KEY = "secret_key"  # noqa: S105

# ------------- LOGGING -------------
LOGGING = {}

# ------------- MIDDLEWARES -------------
MIDDLEWARE = list(filter(lambda x: "DebugToolbarMiddleware" not in x, MIDDLEWARE))

# ------------- PASSWORDS -------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

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
