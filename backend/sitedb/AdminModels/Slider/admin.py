from django.contrib import admin
from django.utils.html import format_html

from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget


class SliderAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }

    list_display = ("title", "show_image", "is_active", "created_at")
    date_hierarchy = "created_at"
    search_fields = ("title", "text", "id")
    actions = [
        "change_slider_status_action",
    ]

    class Media:
        css = {"all": ("css/ImageUploader.css",)}

    def show_image(self, obj):
        image = obj.image.url
        return format_html(
            '<img src="{}" style="width: 100px; height: 100px; object-fit: cover;" />'.format(
                image
            )
        )

    def change_slider_status_action(self, request, queryset):
        queryset.update(is_active=not queryset.values_list("is_active", flat=True)[0])

    show_image.short_description = "Изображение"
    change_slider_status_action.short_description = "Изменить статус"
