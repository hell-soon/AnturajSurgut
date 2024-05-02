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
from DB.models import ProductInfo


class OrderItemsInline(admin.StackedInline):
    model = OrderItems
    extra = 0
    readonly_fields = ["product", "color", "size", "quantity", "cost", "total_cost"]


class OrderAddressInline(admin.StackedInline):
    model = OrderAddress
    extra = 1
    max_num = 1


class LegalDateAdmin(admin.StackedInline):
    model = LegalDate
    extra = 1
    max_num = 1


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
