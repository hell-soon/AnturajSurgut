from django.contrib import admin


class UtilsAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

    list_display_links = ("id", "name")

    list_per_page = 40

    list_max_show_all = 300
