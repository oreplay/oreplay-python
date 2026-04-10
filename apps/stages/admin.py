from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import StageOrders, Stages, StageTypes


@admin.register(StageTypes)
class StageTypesAdmin(TimestampedModelAdmin):
    list_display = ["id", "description", "created"]
    search_fields = ["description"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]


@admin.register(Stages)
class StagesAdmin(TimestampedModelAdmin):
    list_display = [
        "id",
        "event",
        "stage_type",
        "description",
        "order_number",
        "created",
    ]
    search_fields = ["description"]
    list_filter = ["event", "stage_type", "order_number"]
    list_select_related = ["event", "stage_type"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]


@admin.register(StageOrders)
class StageOrdersAdmin(TimestampedModelAdmin):
    list_display = [
        "id",
        "event",
        "stage",
        "original_stage",
        "stage_order",
        "description",
        "created",
    ]
    search_fields = ["description"]
    list_filter = ["event", "stage_order"]
    list_select_related = ["event", "stage", "original_stage"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
