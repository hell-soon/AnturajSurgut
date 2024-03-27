from django.contrib import admin
from ...Tasks.Notify.Sertificate.email import send_sertificate_email


class SertificateAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "quanity",
        "discount",
        "created_at",
        "end_date",
        "status",
        "personal",
    )
    # readonly_fields = ("status",)
    actions = ["send_notification_action"]

    def send_notification_action(self, request, queryset):
        for sertificate in queryset:
            send_sertificate_email(sertificate)

    send_notification_action.short_description = "Отправить уведомление о сертификатах"
