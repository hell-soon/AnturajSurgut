from django.contrib import admin


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "image")
