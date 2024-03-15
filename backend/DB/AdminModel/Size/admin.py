from django.contrib import admin

from DB.models import Size


class SizeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name", "id")
    list_display_links = ("id", "name")
