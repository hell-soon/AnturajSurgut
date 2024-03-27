from django.contrib import admin


class SliderAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "is_active", "created_at")
