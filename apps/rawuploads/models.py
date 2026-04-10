from apps.shared_models import BaseUnmanagedModel
from django.db import models


class RawUploads(BaseUnmanagedModel):
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="raw_uploads_rows",
    )
    stage = models.ForeignKey(
        "stages.Stages",
        on_delete=models.DO_NOTHING,
        db_column="stage_id",
        null=True,
        blank=True,
        related_name="raw_uploads_rows",
    )
    upload_log = models.ForeignKey(
        "uploadlogs.UploadLogs",
        on_delete=models.DO_NOTHING,
        db_column="upload_log_id",
        null=True,
        blank=True,
        related_name="raw_uploads_rows",
    )
    file_data = models.TextField(null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "raw_uploads"

    def __str__(self):
        return f"RawUpload {self.id}"
