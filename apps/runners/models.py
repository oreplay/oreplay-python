from apps.shared_models import BaseUnmanagedModel
from django.db import models


class Runners(BaseUnmanagedModel):
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="runners_rows",
    )
    stage = models.ForeignKey(
        "stages.Stages",
        on_delete=models.DO_NOTHING,
        db_column="stage_id",
        null=True,
        blank=True,
        related_name="runners_rows",
    )
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    klass = models.ForeignKey(
        "classes.Classes",
        on_delete=models.DO_NOTHING,
        db_column="class_id",
        null=True,
        blank=True,
        related_name="runners_rows",
    )
    club = models.ForeignKey(
        "clubs.Clubs",
        on_delete=models.DO_NOTHING,
        db_column="club_id",
        null=True,
        blank=True,
        related_name="runners_rows",
    )
    team = models.ForeignKey(
        "teams.Teams",
        on_delete=models.DO_NOTHING,
        db_column="team_id",
        null=True,
        blank=True,
        related_name="runners_rows",
    )
    db_id = models.CharField(max_length=100, null=True, blank=True)
    sicard = models.CharField(max_length=50, null=True, blank=True)
    bib_number = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    leg_number = models.IntegerField(null=True, blank=True)
    is_nc = models.BooleanField(default=False)
    eligibility = models.CharField(max_length=50, null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "runners"

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name or f"Runner {self.id}"


class RunnerResults(BaseUnmanagedModel):
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="runner_results_rows",
    )
    stage = models.ForeignKey(
        "stages.Stages",
        on_delete=models.DO_NOTHING,
        db_column="stage_id",
        null=True,
        blank=True,
        related_name="runner_results_rows",
    )
    runner = models.ForeignKey(
        "Runners",
        on_delete=models.DO_NOTHING,
        db_column="runner_id",
        null=True,
        blank=True,
        related_name="runner_results_rows",
    )
    klass = models.ForeignKey(
        "classes.Classes",
        on_delete=models.DO_NOTHING,
        db_column="class_id",
        null=True,
        blank=True,
        related_name="runner_results_rows",
    )
    result_type = models.ForeignKey(
        "resulttypes.ResultTypes",
        on_delete=models.DO_NOTHING,
        db_column="result_type_id",
        null=True,
        blank=True,
        related_name="runner_results_rows",
    )
    upload_hash = models.CharField(max_length=255, null=True, blank=True)
    upload_type = models.CharField(max_length=100, null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)
    status_code = models.IntegerField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    finish_time = models.DateTimeField(null=True, blank=True)
    time_seconds = models.IntegerField(null=True, blank=True)
    time_behind = models.IntegerField(null=True, blank=True)
    time_adjusted = models.IntegerField(null=True, blank=True)
    time_penalty = models.IntegerField(null=True, blank=True)
    time_bonus = models.IntegerField(null=True, blank=True)
    time_neutralization = models.IntegerField(null=True, blank=True)
    points_final = models.DecimalField(
        max_digits=12, decimal_places=3, null=True, blank=True
    )
    points_adjusted = models.DecimalField(
        max_digits=12, decimal_places=3, null=True, blank=True
    )
    points_penalty = models.DecimalField(
        max_digits=12, decimal_places=3, null=True, blank=True
    )
    points_bonus = models.DecimalField(
        max_digits=12, decimal_places=3, null=True, blank=True
    )
    stage_order = models.IntegerField(null=True, blank=True)
    leg_number = models.IntegerField(null=True, blank=True)
    is_nc = models.BooleanField(default=False)
    contributory = models.BooleanField(default=False)
    note = models.TextField(null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "runner_results"

    def __str__(self):
        return f"Result {self.position}" if self.position else f"Result {self.id}"
