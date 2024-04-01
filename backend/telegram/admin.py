from django.contrib import admin
from .models import TelegramNews, TelegramImage
from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget
from django.utils.html import format_html


class TelegramImageInline(admin.TabularInline):
    model = TelegramNews.image.through
    extra = 1


@admin.register(TelegramNews)
class TelegramNewsAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]


@admin.register(TelegramImage)
class TelegramImageAdmin(admin.ModelAdmin):
    list_display = ["id", "show_image"]
    list_display_links = ["id", "show_image"]

    class Media:
        css = {"all": ("css/ImageUploader.css",)}

    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }

    def show_image(self, obj):
        image = obj.image.url
        return format_html(
            '<img src="{}" style="width: 100px; height: 100px; object-fit: cover;" />'.format(
                image
            )
        )

    show_image.short_description = "Изображение"
