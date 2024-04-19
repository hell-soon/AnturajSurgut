from django.contrib import admin


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "is_active")
