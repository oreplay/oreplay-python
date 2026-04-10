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
        "klass",
        "club",
        "bib_number",
        "is_nc",
        "created",
    ]
    search_fields = ["team_name"]
    list_filter = ["event", "stage", "is_nc"]
    list_select_related = ["event", "stage", "klass", "club"]
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
        "klass",
        "position",
        "status_code",
        "time_seconds",
        "points_final",
        "is_nc",
        "created",
    ]
    search_fields = ["team__team_name"]
    list_filter = [
        "event",
        "stage",
        "is_nc",
        "contributory",
        "status_code",
        "result_type",
    ]
    list_select_related = ["event", "stage", "team", "klass", "result_type"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
