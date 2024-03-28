from django.contrib import admin


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "url", "created_at")
