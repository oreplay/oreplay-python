from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import TeamResults, Teams


@admin.register(Teams)
class TeamsAdmin(TimestampedModelAdmin):
    list_display = [
        "id",
        "event",
        "stage",
        "team_name",
        "entry_class",
        "club",
        "bib_number",
        "is_nc",
        "created",
    ]
    search_fields = ["team_name"]
    list_filter = ["event", "stage", "is_nc"]
    list_select_related = ["event", "stage", "entry_class", "club"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]


@admin.register(TeamResults)
class TeamResultsAdmin(TimestampedModelAdmin):
    list_display = [
        "id",
        "event",
        "stage",
        "team",
        "entry_class",
        "position",
        "status_code",
        "time_seconds",
        "points_final",
        "created",
    ]
    search_fields = ["team__team_name"]
    list_filter = [
        "event",
        "stage",
        "status_code",
        "result_type",
    ]
    list_select_related = ["event", "stage", "team", "entry_class", "result_type"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
