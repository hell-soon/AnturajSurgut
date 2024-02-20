from django.contrib import admin
from .models import TelegramNews, TelegramImage, TelegramImageOrder

# Register your models here.


@admin.register(TelegramNews)
class TelegramNewsAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(TelegramImage)
class TelegramImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


@admin.register(TelegramImageOrder)
class TelegramImageOrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_status",
        "image",
    )
