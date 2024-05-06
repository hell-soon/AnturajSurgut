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
    readonly_fields = [
        "city",
        "region",
        "post_index",
        "floor",
        "street",
        "house",
        "apartment",
    ]


class LegalDateAdmin(admin.StackedInline):
    model = LegalDate
    extra = 1
    max_num = 1
    readonly_fields = [
        "name",
        "inn",
        "kpp",
        "ogrn",
        "bik",
        "bank_name",
        "cores_account",
        "ras_check",
        "legal_address",
    ]


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
