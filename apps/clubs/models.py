from apps.shared_models import BaseUnmanagedModel
from django.db import models


class Clubs(BaseUnmanagedModel):
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="clubs_rows",
    )
    stage = models.ForeignKey(
        "stages.Stages",
        on_delete=models.DO_NOTHING,
        db_column="stage_id",
        null=True,
        blank=True,
        related_name="clubs_rows",
    )
    oe_key = models.CharField(max_length=50, null=True, blank=True)
    short_name = models.CharField(max_length=100, null=True, blank=True)
    long_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "clubs"

    def __str__(self):
        return self.short_name or self.long_name or f"Club {self.id}"
