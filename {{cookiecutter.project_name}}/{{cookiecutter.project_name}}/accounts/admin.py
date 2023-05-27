from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from {{ cookiecutter.project_name }}.accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass
