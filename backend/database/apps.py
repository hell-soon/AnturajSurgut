from django.apps import AppConfig


class DatabaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "database"
    verbose_name = "База данных"

    def ready(self):
        from . import signals
