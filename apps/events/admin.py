from apps.admin_base import TimestampedModelAdmin
from django.contrib import admin

from .models import Events


@admin.register(Events)
class EventsAdmin(TimestampedModelAdmin):
    list_display = [
        "id",
        "description",
        "scope",
        "location",
        "country_code",
        "is_hidden",
        "initial_date",
        "final_date",
        "created",
    ]
    search_fields = ["description", "location", "scope"]
    list_filter = ["is_hidden", "country_code", "scope"]
    list_select_related = ["federation", "organizer"]
    list_per_page = 50
    show_full_result_count = False
    ordering = ["-created"]
