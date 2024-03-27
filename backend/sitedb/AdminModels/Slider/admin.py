from django.contrib import admin
from django.utils.html import format_html


class SliderAdmin(admin.ModelAdmin):
    list_display = ("title", "show_image", "is_active", "created_at")

    def show_image(self, obj):
        image = obj.image.url
        return format_html('<img src="{}" width="75" height="75" />'.format(image))

    show_image.short_description = "Картинка"
