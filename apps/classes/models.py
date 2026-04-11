from apps.shared_models import BaseUnmanagedModel
from django.db import models


class Classes(BaseUnmanagedModel):
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="classes_rows",
    )
    stage = models.ForeignKey(
        "stages.Stages",
        on_delete=models.DO_NOTHING,
        db_column="stage_id",
        null=True,
        blank=True,
        related_name="classes_rows",
    )
    oe_key = models.CharField(max_length=50, null=True, blank=True)
    short_name = models.CharField(max_length=100, null=True, blank=True)
    long_name = models.CharField(max_length=255, null=True, blank=True)
    course = models.ForeignKey(
        "courses.Courses",
        on_delete=models.DO_NOTHING,
        db_column="course_id",
        null=True,
        blank=True,
        related_name="classes_rows",
    )
    upload_hash = models.CharField(max_length=255, null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "classes"

    def __str__(self):
        return self.short_name or self.long_name or f"Class {self.id}"


class ClassesControls(BaseUnmanagedModel):
    id = None
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="classes_controls_rows",
    )
    stage = models.ForeignKey(
        "stages.Stages",
        on_delete=models.DO_NOTHING,
        db_column="stage_id",
        null=True,
        blank=True,
        related_name="classes_controls_rows",
    )
    control_class = models.ForeignKey(
        "Classes",
        on_delete=models.DO_NOTHING,
        db_column="class_id",
        primary_key=True,
        related_name="classes_controls_rows",
    )
    control = models.ForeignKey(
        "controls.Controls",
        on_delete=models.DO_NOTHING,
        db_column="control_id",
        null=True,
        blank=True,
        related_name="classes_controls_rows",
    )
    order_number = models.IntegerField(null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "classes_controls"

    def __str__(self):
        return f"ClassControl {self.control_class_id}:{self.control_id}:{self.order_number}"
