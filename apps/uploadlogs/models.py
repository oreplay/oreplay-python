from apps.shared_models import BaseUnmanagedModel
from django.db import models


class UploadLogs(BaseUnmanagedModel):
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="upload_logs_rows",
    )
    stage = models.ForeignKey(
        "stages.Stages",
        on_delete=models.DO_NOTHING,
        db_column="stage_id",
        null=True,
        blank=True,
        related_name="upload_logs_rows",
    )
    upload_type = models.CharField(max_length=100, null=True, blank=True)
    upload_status = models.IntegerField(null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "upload_logs"

    def __str__(self):
        return (
            f"UploadLog {self.upload_type}"
            if self.upload_type
            else f"UploadLog {self.id}"
        )
