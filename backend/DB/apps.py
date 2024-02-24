from django.apps import AppConfig


class DbConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "DB"

    verbose_name = "База данных"
    verbose_name_plural = "База данных"
