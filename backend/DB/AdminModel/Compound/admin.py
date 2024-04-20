from django.contrib import admin


class CompoundAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    search_fields = (
        "name",
        "id",
    )
    list_display_links = ("name",)
