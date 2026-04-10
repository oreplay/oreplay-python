from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import Tokens


@admin.register(Tokens)
class TokensAdmin(TimestampedModelAdmin):
    list_display = ["id", "token", "foreign_model", "expires", "created"]
    search_fields = ["token", "foreign_model"]
    list_filter = ["foreign_model"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
