from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import Controls, ControlTypes


@admin.register(ControlTypes)
class ControlTypesAdmin(TimestampedModelAdmin):
    list_display = ["id", "description", "created"]
    search_fields = ["description"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]


@admin.register(Controls)
class ControlsAdmin(TimestampedModelAdmin):
    list_display = ["id", "event", "stage", "station", "control_type", "created"]
    search_fields = ["station"]
    list_filter = ["event", "stage", "control_type"]
    list_select_related = ["event", "stage", "control_type"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
