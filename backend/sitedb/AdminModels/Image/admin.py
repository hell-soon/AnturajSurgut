from django.contrib import admin
from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget


class SiteImageAdmin(admin.ModelAdmin):
    list_display = ("image",)

    class Media:
        css = {
            "all": ("css/ImageUploader.css",),
        }

    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }
