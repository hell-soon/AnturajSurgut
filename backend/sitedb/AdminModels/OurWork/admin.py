from django.contrib import admin


class OurWorkAdmin(admin.ModelAdmin):
    list_display = ("title", "work_list", "description")
