from django.contrib import admin


class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
