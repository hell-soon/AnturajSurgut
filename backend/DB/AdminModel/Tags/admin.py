from django.contrib import admin

from DB.models import Tags


class TagsAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name", "id")
