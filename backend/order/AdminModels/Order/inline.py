from django.contrib import admin
from order.models import OrderItems, OrderAddress


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 1
    readonly_fields = [
        "color",
        "size",
        "cost",
        "total_cost",
    ]


class OrderAddressInline(admin.TabularInline):
    model = OrderAddress
    extra = 1
    fields = ["region", "city", "street", "house", "apartment", "floor", "post_index"]

    class Media:
        css = {
            "all": ("css/Fields.css",),
        }
