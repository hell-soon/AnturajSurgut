from django.contrib import admin
from .models import TelegramNews, TelegramImage

# Register your models here.


@admin.register(TelegramNews)
class TelegramNewsAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(TelegramImage)
class TelegramImageAdmin(admin.ModelAdmin):
    list_display = ("image",)
