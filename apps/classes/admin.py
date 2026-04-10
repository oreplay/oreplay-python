from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import Classes, ClassesControls


@admin.register(Classes)
class ClassesAdmin(TimestampedModelAdmin):
    list_display = [
        "id",
        "event",
        "stage",
        "short_name",
        "long_name",
        "oe_key",
        "course",
        "created",
    ]
    search_fields = ["short_name", "long_name", "oe_key"]
    list_filter = ["event", "stage"]
    list_select_related = ["event", "stage", "course"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]


@admin.register(ClassesControls)
class ClassesControlsAdmin(TimestampedModelAdmin):
    list_display = [
        "id",
        "event",
        "stage",
        "klass",
        "control",
        "order_number",
        "created",
    ]
    search_fields = ["order_number"]
    list_filter = ["event", "stage", "order_number"]
    list_select_related = ["event", "stage", "klass", "control"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
