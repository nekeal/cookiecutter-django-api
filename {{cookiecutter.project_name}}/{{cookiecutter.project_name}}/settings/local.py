from .base import *

SECRET_KEY = "secret_key"

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
