from django.apps import AppConfig


class TelegramConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "telegram"
    verbose_name = "Телеграмм"

    def ready(self):
        from . import signals
