from apps.shared_models import BaseUnmanagedModel
from django.db import models


class Splits(BaseUnmanagedModel):
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="splits_rows",
    )
    stage = models.ForeignKey(
        "stages.Stages",
        on_delete=models.DO_NOTHING,
        db_column="stage_id",
        null=True,
        blank=True,
        related_name="splits_rows",
    )
    runner = models.ForeignKey(
        "runners.Runners",
        on_delete=models.DO_NOTHING,
        db_column="runner_id",
        null=True,
        blank=True,
        related_name="splits_rows",
    )
    runner_result = models.ForeignKey(
        "runners.RunnerResults",
        on_delete=models.DO_NOTHING,
        db_column="runner_result_id",
        null=True,
        blank=True,
        related_name="splits_rows",
    )
    team_result = models.ForeignKey(
        "teams.TeamResults",
        on_delete=models.DO_NOTHING,
        db_column="team_result_id",
        null=True,
        blank=True,
        related_name="splits_rows",
    )
    klass = models.ForeignKey(
        "classes.Classes",
        on_delete=models.DO_NOTHING,
        db_column="class_id",
        null=True,
        blank=True,
        related_name="splits_rows",
    )
    control = models.ForeignKey(
        "controls.Controls",
        on_delete=models.DO_NOTHING,
        db_column="control_id",
        null=True,
        blank=True,
        related_name="splits_rows",
    )
    sicard = models.CharField(max_length=50, null=True, blank=True)
    station = models.IntegerField(null=True, blank=True)
    points = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    order_number = models.IntegerField(null=True, blank=True)
    is_intermediate = models.BooleanField(default=False)
    reading_time = models.DateTimeField(null=True, blank=True)
    battery_perc = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    battery_time = models.DateTimeField(null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "splits"

    def __str__(self):
        return f"Split {self.station}" if self.station else f"Split {self.id}"
