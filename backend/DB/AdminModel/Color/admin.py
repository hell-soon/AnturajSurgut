from django.contrib import admin
from django.utils.html import format_html

from DB.models import Color


class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "color_indicator")
    search_fields = ("name", "id")
    list_display_links = ("id", "name")

    def color_indicator(self, obj):
        return format_html(
            '<div style="background-color: {}; width: 25px; height: 25px; border: 1px solid black"></div>',
            obj.color,
        )

    color_indicator.short_description = "Цвет"
