from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import AccessToken, User


@admin.register(User)
class UserAdmin(TimestampedModelAdmin):
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_admin",
        "is_super",
        "is_staff",
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    list_filter = (
        "is_admin",
        "is_super",
    )
    readonly_fields = (
        "username",
        "is_staff",
        "is_superuser",
    )


@admin.register(AccessToken)
class AccessTokenAdmin(TimestampedModelAdmin):
    list_display = (
        "access_token",
        "client_id",
        "user",
        "expires",
    )
    search_fields = (
        "access_token",
        "client_id",
        "user__email",
    )
    list_select_related = ("user",)
