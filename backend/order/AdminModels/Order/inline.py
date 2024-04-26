from django.contrib import admin
from order.models import (
    OrderItems,
    OrderAddress,
    LegalDate,
    OrderStatus,
    OrderType,
    OrderFace,
    PaymentType,
)


class OrderItemsInline(admin.TabularInline):
    model = OrderItems

    extra = 1
    readonly_fields = [
        "color",
        "size",
        "cost",
        "total_cost",
    ]


class OrderAddressInline(admin.StackedInline):
    model = OrderAddress
    extra = 1
    max_num = 1
    fields = ["region", "city", "street", "house", "apartment", "floor", "post_index"]

    def get_extra(self, request, obj=None, **kwargs):
        if not obj:
            return self.extra
        if self.model.objects.filter(order=obj).exists():
            return 0
        return self.extra


class LegalDateAdmin(admin.StackedInline):
    model = LegalDate
    extra = 1
    max_num = 1

    def get_extra(self, request, obj=None, **kwargs):
        if not obj:
            return self.extra
        if self.model.objects.filter(order=obj).exists():
            return 0
        return self.extra


class OrderStatusInline(admin.TabularInline):
    model = OrderStatus
    extra = 1


class OrderTypeInline(admin.TabularInline):
    model = OrderType
    extra = 1


class OrderFaceInline(admin.TabularInline):
    model = OrderFace
    extra = 1


class PaymentTypeInline(admin.TabularInline):
    model = PaymentType
    extra = 1
