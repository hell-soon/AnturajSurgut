from django.contrib import admin
from DB.models import SubCatalog
from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget


class SubCatalogAdmin(admin.TabularInline):
    model = SubCatalog
    extra = 0  # fields to show in admin

    class Media:
        css = {
            "all": ("css/ImageUploader.css",),
        }

    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }
