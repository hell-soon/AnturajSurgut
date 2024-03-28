from django.contrib import admin
from order.models import OrderItems


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 1
    readonly_fields = [
        "color",
        "size",
        "cost",
        "total_cost",
    ]
