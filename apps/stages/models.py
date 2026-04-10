from apps.shared_models import BaseUnmanagedModel
from django.db import models


class StageTypes(BaseUnmanagedModel):
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "stage_types"

    def __str__(self):
        return self.description or f"StageType {self.id}"


class Stages(BaseUnmanagedModel):
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="stages_rows",
    )
    stage_type = models.ForeignKey(
        "StageTypes",
        on_delete=models.DO_NOTHING,
        db_column="stage_type_id",
        null=True,
        blank=True,
        related_name="stages_rows",
    )
    description = models.CharField(max_length=255, null=True, blank=True)
    base_date = models.DateField(null=True, blank=True)
    base_time = models.TimeField(null=True, blank=True)
    order_number = models.IntegerField(null=True, blank=True)
    server_offset = models.IntegerField(null=True, blank=True)
    utc_value = models.IntegerField(null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "stages"

    def __str__(self):
        return self.description or f"Stage {self.id}"


class StageOrders(BaseUnmanagedModel):
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="stage_orders_rows",
    )
    stage = models.ForeignKey(
        "Stages",
        on_delete=models.DO_NOTHING,
        db_column="stage_id",
        null=True,
        blank=True,
        related_name="stage_orders_rows",
    )
    original_stage = models.ForeignKey(
        "Stages",
        on_delete=models.DO_NOTHING,
        db_column="original_stage_id",
        null=True,
        blank=True,
        related_name="original_stage_orders_rows",
    )
    stage_order = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "stage_orders"

    def __str__(self):
        return self.description or f"StageOrder {self.id}"
