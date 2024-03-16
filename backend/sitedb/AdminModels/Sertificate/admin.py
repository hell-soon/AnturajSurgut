from django.contrib import admin


class SertificateAdmin(admin.ModelAdmin):
    list_display = ("code", "quanity", "discount", "created_at", "end_date", "status")
    # readonly_fields = ("status",)
