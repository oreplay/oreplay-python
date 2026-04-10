from apps.shared_models import BaseUnmanagedModel
from django.db import models


class UsersEvents(BaseUnmanagedModel):
    id = None
    user = models.ForeignKey(
        "users.User",
        on_delete=models.DO_NOTHING,
        db_column="user_id",
        primary_key=True,
        related_name="users_events_rows",
    )
    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        related_name="users_events_rows",
    )

    class Meta(BaseUnmanagedModel.Meta):
        db_table = "users_events"

    def __str__(self):
        return f"UserEvent {self.user_id} -> {self.event_id}"
