from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import Ranking


@admin.register(Ranking)
class RankingAdmin(TimestampedModelAdmin):
    list_display = (
        "id",
        "event",
        "stage",
        "max_points",
        "round_precision",
        "nc_true",
        "nc_false",
        "created",
    )
    search_fields = (
        "id",
        "event__id",
        "stage__id",
        "status_scores",
        "excluded_class_names",
    )
