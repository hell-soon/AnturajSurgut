from django.contrib import admin
from .models import *


@admin.register(Additionalservices)
class AdditionalservicesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
    )


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin View for Order"""

    list_display = (
        "order_number",
        "user_initials",
        "user_email",
        "user_phone",
        "created_at",
        "order_type",
        "order_address",
        "order_face",
        "get_additional_services",
        "order_paymant",
        "order_status",
        "comment",
        "track_number",
    )
    list_filter = ("order_type", "order_status")
    inlines = [OrderItemsInline]

    def get_additional_services(self, obj):
        additional_services = obj.order_additionalservices.all()
        if additional_services:
            return ", ".join([str(service) for service in additional_services])
        else:
            return "Нету дополнительных услуг"

    get_additional_services.short_description = "Дополнительные услуги"


admin.site.register(OrderItems)
