from django.contrib import admin
from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget
from .inline import ServiceSliderInline, ServiceOurWorkInline


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "created_at")
    inlines = [ServiceSliderInline, ServiceOurWorkInline]

    class Media:
        css = {
            "all": ("css/ImageUploader.css",),
        }

    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }
