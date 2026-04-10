from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import Clubs


@admin.register(Clubs)
class ClubsAdmin(TimestampedModelAdmin):
    list_display = [
        "id",
        "short_name",
        "long_name",
        "oe_key",
        "event",
        "stage",
        "created",
    ]
    search_fields = ["short_name", "long_name", "oe_key"]
    list_filter = ["event", "stage"]
    list_select_related = ["event", "stage"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
