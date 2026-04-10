from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import Courses


@admin.register(Courses)
class CoursesAdmin(TimestampedModelAdmin):
    list_display = [
        "id",
        "event",
        "stage",
        "short_name",
        "long_name",
        "distance",
        "climb",
        "created",
    ]
    search_fields = ["short_name", "long_name", "oe_key"]
    list_filter = ["event", "stage"]
    list_select_related = ["event", "stage"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
