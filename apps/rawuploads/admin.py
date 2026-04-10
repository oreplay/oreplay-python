from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import RawUploads


@admin.register(RawUploads)
class RawUploadsAdmin(TimestampedModelAdmin):
    list_display = ["id", "event", "stage", "upload_log", "created"]
    search_fields = ["file_data"]
    list_filter = ["event", "stage"]
    list_select_related = ["event", "stage", "upload_log"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
