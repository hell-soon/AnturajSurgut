from django.contrib import admin
from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "created_at")
    
    filter_horizontal = ["slider","our_work"]
    class Media:
        css = {
            "all": ("css/ImageUploader.css",),
        }

    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }
