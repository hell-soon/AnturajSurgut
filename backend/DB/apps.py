from django.apps import AppConfig


class DbConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "DB"

    verbose_name = "Каталог товаров"
    verbose_name_plural = "База данных"

    def ready(self):
        from . import signals
