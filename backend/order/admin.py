from django.contrib import admin
from .models import *
from .AdminModels import OrderAdmin, AdditionalservicesAdmin, UtilsAdmin

from .AdminModels.Order.inline import (
    OrderTypeInline,
    OrderFaceInline,
    OrderStatusInline,
    PaymentTypeInline,
)


class OrderSettingsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    inlines = [OrderTypeInline, OrderFaceInline, OrderStatusInline, PaymentTypeInline]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(OrderSettings, OrderSettingsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Additionalservices, AdditionalservicesAdmin)
