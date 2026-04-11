from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import Splits


@admin.register(Splits)
class SplitsAdmin(TimestampedModelAdmin):
    list_display = [
        "id",
        "event",
        "stage",
        "runner",
        "station",
        "order_number",
        "is_intermediate",
        "reading_time",
        "created",
    ]
    search_fields = ["sicard", "station"]
    list_filter = ["event", "stage", "is_intermediate"]
    list_select_related = [
        "event",
        "stage",
        "runner",
        "runner_result",
        "team_result",
        "entry_class",
        "control",
    ]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
