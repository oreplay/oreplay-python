from apps.shared_models import BaseUnmanagedModel
from django.db import models


class Courses(BaseUnmanagedModel):
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="courses_rows",
    )
    stage = models.ForeignKey(
        "stages.Stages",
        on_delete=models.DO_NOTHING,
        db_column="stage_id",
        null=True,
        blank=True,
        related_name="courses_rows",
    )
    short_name = models.CharField(max_length=100, null=True, blank=True)
    long_name = models.CharField(max_length=255, null=True, blank=True)
    oe_key = models.CharField(max_length=50, null=True, blank=True)
    distance = models.FloatField(null=True, blank=True)
    climb = models.FloatField(null=True, blank=True)
    controls = models.TextField(null=True, blank=True)
    coord_system = models.CharField(max_length=50, null=True, blank=True)
    datum = models.CharField(max_length=50, null=True, blank=True)
    utm_zone = models.CharField(max_length=20, null=True, blank=True)
    hemisphere = models.CharField(max_length=10, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    zoom = models.IntegerField(null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "courses"

    def __str__(self):
        return self.short_name or self.long_name or f"Course {self.id}"
