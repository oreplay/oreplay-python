from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import RunnerResults, Runners


@admin.register(Runners)
class RunnersAdmin(TimestampedModelAdmin):
    list_display = [
        "id",
        "event",
        "stage",
        "first_name",
        "last_name",
        "sicard",
        "bib_number",
        "sex",
        "is_nc",
        "created",
    ]
    search_fields = ["first_name", "last_name", "sicard"]
    list_filter = ["event", "stage", "is_nc", "sex"]
    list_select_related = ["event", "stage", "klass", "club", "team"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]


@admin.register(RunnerResults)
class RunnerResultsAdmin(TimestampedModelAdmin):
    list_display = [
        "id",
        "event",
        "stage",
        "runner",
        "klass",
        "position",
        "status_code",
        "time_seconds",
        "points_final",
        "is_nc",
        "created",
    ]
    search_fields = ["runner__first_name", "runner__last_name"]
    list_filter = [
        "event",
        "stage",
        "is_nc",
        "contributory",
        "status_code",
        "result_type",
    ]
    list_select_related = ["event", "stage", "runner", "klass", "result_type"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
