from django.contrib import admin
from django.utils.html import format_html

from DB.models import Catalog
from ..SubCatalogInline.inline import SubCatalogAdmin
from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget


class CatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image_preview")
    list_display_links = ("id", "name")
    search_fields = ("name", "id")
    inlines = [SubCatalogAdmin]

    class Media:
        css = {
            "all": ("css/ImageUploader.css",),
        }

    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="75" height="75" style="object-fit: cover;"/>',
                obj.image.url,
            )
        else:
            return "-"

    image_preview.short_description = "Изображение"
