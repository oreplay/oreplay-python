from apps.shared_models import BaseUnmanagedModel
from django.db import models


class Tokens(BaseUnmanagedModel):
    token = models.CharField(max_length=255, null=True, blank=True)
    foreign_key = models.CharField(max_length=36, null=True, blank=True)
    foreign_model = models.CharField(max_length=120, null=True, blank=True)
    expires = models.DateTimeField(null=True, blank=True)

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "tokens"

    def __str__(self):
        return f"Token {self.token[:10]}" if self.token else f"Token {self.id}"
