from django.contrib import admin

from DB.models import Type


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
