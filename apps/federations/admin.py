from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import Federations


@admin.register(Federations)
class FederationsAdmin(TimestampedModelAdmin):
    list_display = ["id", "description", "created"]
    search_fields = ["description"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
