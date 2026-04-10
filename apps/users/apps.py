from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"

    def ready(self):
        from apps.shared_models import normalize_unmanaged_model_names

        normalize_unmanaged_model_names()
