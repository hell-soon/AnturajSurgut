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

    def show_image(self, obj):
        image = obj.image.url
        return format_html(
            '<img src="{}" style="width: 100px; height: 100px; object-fit: cover;" />'.format(
                image
            )
        )

    def change_slider_status_action(self, request, queryset):
        for item in queryset:
            if item.is_active:
                item.is_active = False
            else:
                item.is_active = True
            item.save()

    show_image.short_description = "Изображение"
    change_slider_status_action.short_description = "Изменить статус"
