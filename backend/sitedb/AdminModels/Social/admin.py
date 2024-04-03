from django.contrib import admin
from django.utils.html import format_html

from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget


class SocailAdmin(admin.ModelAdmin):
    list_display = ["name", "url", "show_icon"]

    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }

    class Media:
        css = {"all": ("css/ImageUploader.css",)}

    def show_icon(self, obj):
        icon = obj.icon.url
        return format_html(
            '<img src="{}" style="width: 100px; height: 100px; object-fit: cover;" />'.format(
                icon
            )
        )

    show_icon.short_description = "Иконка"
