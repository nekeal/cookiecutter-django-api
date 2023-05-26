from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from recevent_printing_manager.accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass
