import uuid

from django.db import models
from django.utils.timezone import now


class Organizer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    external_id = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    deleted = models.DateTimeField(null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.deleted = now()
        self.save()

    objects = models.Manager()

    class Meta:
        db_table = "organizers"
