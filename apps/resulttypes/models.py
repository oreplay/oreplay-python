from apps.shared_models import BaseUnmanagedModel
from django.db import models


class ResultTypes(BaseUnmanagedModel):
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "result_types"

    def __str__(self):
        return self.description or f"ResultTypes {self.id}"
