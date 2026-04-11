from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import UsersEvents


@admin.register(UsersEvents)
class UsersEventsAdmin(TimestampedModelAdmin):
    list_display = ["user", "event", "created"]
    search_fields = ["user__email", "event__description"]
    list_filter = ["event"]
    list_select_related = ["user", "event"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
