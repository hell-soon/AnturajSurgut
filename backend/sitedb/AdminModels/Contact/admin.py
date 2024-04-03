from django.contrib import admin


class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "fax")
    