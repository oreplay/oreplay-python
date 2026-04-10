from apps.shared_models import BaseUnmanagedModel
from django.db import models


class Events(BaseUnmanagedModel):
    description = models.TextField(null=True, blank=True)
    scope = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    country_code = models.CharField(max_length=10, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    picture = models.CharField(max_length=255, null=True, blank=True)
    initial_date = models.DateField(null=True, blank=True)
    final_date = models.DateField(null=True, blank=True)
    is_hidden = models.BooleanField(default=False)
    federation = models.ForeignKey(
        "federations.Federations",
        on_delete=models.DO_NOTHING,
        db_column="federation_id",
        null=True,
        blank=True,
        related_name="events_rows",
    )
    organizer = models.ForeignKey(
        "organizers.Organizer",
        on_delete=models.DO_NOTHING,
        db_column="organizer_id",
        null=True,
        blank=True,
        related_name="events_rows",
    )

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "events"

    def __str__(self):
        return self.description or f"Event {self.id}"
