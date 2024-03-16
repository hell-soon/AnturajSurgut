from django.contrib import admin


class AdditionalservicesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "cost",
    )
