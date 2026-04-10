from django.contrib import admin
from django.utils import timezone


class TimestampedModelAdmin(admin.ModelAdmin):
    timestamp_fields = ("created", "modified", "deleted")

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super().get_readonly_fields(request, obj))
        for field_name in self.timestamp_fields:
            if (
                field_name in {field.name for field in self.model._meta.fields}
                and field_name not in readonly_fields
            ):
                readonly_fields.append(field_name)
        return readonly_fields

    def save_model(self, request, obj, form, change):
        now = timezone.now()
        field_names = {field.name for field in self.model._meta.fields}

        if (
            "created" in field_names
            and not change
            and getattr(obj, "created", None) is None
        ):
            obj.created = now
        if "modified" in field_names:
            obj.modified = now
        if "deleted" in field_names and getattr(obj, "deleted", None) is None:
            obj.deleted = None

        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        field_names = {field.name for field in self.model._meta.fields}
        if "deleted" in field_names:
            now = timezone.now()
            obj.deleted = now
            if "modified" in field_names:
                obj.modified = now
            obj.save(
                update_fields=[
                    field for field in ("deleted", "modified") if field in field_names
                ]
            )
            return

        super().delete_model(request, obj)

    def delete_queryset(self, request, queryset):
        field_names = {field.name for field in self.model._meta.fields}
        if "deleted" in field_names:
            now = timezone.now()
            update_fields = {"deleted": now}
            if "modified" in field_names:
                update_fields["modified"] = now
            queryset.update(**update_fields)
            return

        super().delete_queryset(request, queryset)
