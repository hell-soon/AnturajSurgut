from django.contrib import admin
from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "image")
    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }

    class Media:
        css = {
            "all": ("css/ImageUploader.css",),
        }
