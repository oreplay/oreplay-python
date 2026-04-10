"""Shared base models for all unmanaged apps."""

from django.apps import apps as django_apps
from django.db import models

VERBOSE_NAME_OVERRIDES = {
    "Classes": "Class",
    "ClassesControls": "Class Control",
    "Clubs": "Club",
    "ControlTypes": "Control Type",
    "Controls": "Control",
    "Courses": "Course",
    "Events": "Event",
    "Federations": "Federation",
    "RawUploads": "Raw Upload",
    "ResultTypes": "Result Type",
    "Runners": "Runner",
    "RunnerResults": "Runner Result",
    "Splits": "Split",
    "StageOrders": "Stage Order",
    "StageTypes": "Stage Type",
    "Stages": "Stage",
    "Teams": "Team",
    "TeamResults": "Team Result",
    "Tokens": "Token",
    "UploadLogs": "Upload Log",
    "UsersEvents": "User Event",
}

VERBOSE_NAME_PLURAL_OVERRIDES = {
    "Classes": "Classes",
}


def normalize_unmanaged_model_names() -> None:
    for model in django_apps.get_models():
        if not issubclass(model, BaseUnmanagedModel) or model._meta.abstract:
            continue

        verbose_name = VERBOSE_NAME_OVERRIDES.get(model.__name__, model.__name__)
        model._meta.verbose_name = verbose_name
        model._meta.verbose_name_plural = VERBOSE_NAME_PLURAL_OVERRIDES.get(
            model.__name__,
            f"{verbose_name}s",
        )


class BaseUnmanagedModel(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    created = models.DateTimeField(null=True, blank=True)
    modified = models.DateTimeField(null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
        managed = False

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if getattr(cls._meta, "abstract", False):
            return

        verbose_name = VERBOSE_NAME_OVERRIDES.get(cls.__name__, cls.__name__)
        cls._meta.verbose_name = verbose_name
        cls._meta.verbose_name_plural = VERBOSE_NAME_PLURAL_OVERRIDES.get(
            cls.__name__,
            f"{verbose_name}s",
        )


class StageScopedModel(BaseUnmanagedModel):
    """Base model for entities scoped to events and stages."""

    event = models.ForeignKey(
        "events.Events",
        on_delete=models.DO_NOTHING,
        db_column="event_id",
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_event",
    )
    stage = models.ForeignKey(
        "stages.Stages",
        on_delete=models.DO_NOTHING,
        db_column="stage_id",
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_stage",
    )

    class Meta(BaseUnmanagedModel.Meta):
        abstract = True
