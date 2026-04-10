from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import UploadLogs


@admin.register(UploadLogs)
class UploadLogsAdmin(TimestampedModelAdmin):
    list_display = [
        "id",
        "event",
        "stage",
        "upload_type",
        "upload_status",
        "state",
        "created",
    ]
    search_fields = ["upload_type", "info"]
    list_filter = ["event", "stage", "upload_type", "upload_status"]
    list_select_related = ["event", "stage"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
