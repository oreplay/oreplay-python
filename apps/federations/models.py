from apps.shared_models import BaseUnmanagedModel
from django.db import models


class Federations(BaseUnmanagedModel):
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "federations"

    def __str__(self):
        return self.description or f"Federations {self.id}"
