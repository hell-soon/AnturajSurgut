from django.contrib import admin
from django.utils.html import format_html

from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview")
    list_display_links = ("id", "image_preview")
    search_fields = ("id",)
    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }

    class Media:
        css = {
            "all": ("css/ImageUploader.css",),
        }

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="75" height="75" style="object-fit: cover;"/>',
                obj.image.url,
            )
        else:
            return "Изображение отсутствует"

    image_preview.short_description = "Изображение"
