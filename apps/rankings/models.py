from django.db import models


class Ranking(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    scoring_algorithm = models.CharField(max_length=150)
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="rankings_rows",
    )
    stage = models.ForeignKey(
        "stages.Stages",
        on_delete=models.DO_NOTHING,
        db_column="stage_id",
        null=True,
        blank=True,
        related_name="rankings_rows",
    )
    max_points = models.DecimalField(
        max_digits=12, decimal_places=3, null=True, blank=True
    )
    round_precision = models.IntegerField(null=True, blank=True)
    nc_true = models.DecimalField(
        max_digits=12, decimal_places=3, null=True, blank=True
    )
    nc_false = models.DecimalField(
        max_digits=12, decimal_places=3, null=True, blank=True
    )
    status_scores = models.TextField(null=True, blank=True)
    excluded_class_names = models.TextField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = "rankings"
