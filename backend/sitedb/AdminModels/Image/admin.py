from django.contrib import admin


class OurWorkImageAdmin(admin.ModelAdmin):
    list_display = ("image",)
