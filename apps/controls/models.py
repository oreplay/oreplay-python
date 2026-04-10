from apps.shared_models import BaseUnmanagedModel
from django.db import models


class ControlTypes(BaseUnmanagedModel):
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "control_types"

    def __str__(self):
        return self.description or f"ControlType {self.id}"


class Controls(BaseUnmanagedModel):
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="controls_rows",
    )
    stage = models.ForeignKey(
        "stages.Stages",
        on_delete=models.DO_NOTHING,
        db_column="stage_id",
        null=True,
        blank=True,
        related_name="controls_rows",
    )
    station = models.IntegerField(null=True, blank=True)
    control_type = models.ForeignKey(
        "ControlTypes",
        on_delete=models.DO_NOTHING,
        db_column="control_type_id",
        null=True,
        blank=True,
        related_name="controls_rows",
    )

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "controls"

    def __str__(self):
        return f"Control {self.station}" if self.station else f"Control {self.id}"
