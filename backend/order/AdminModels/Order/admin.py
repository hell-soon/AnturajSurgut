from django.contrib import admin
from .inline import OrderItemsInline, OrderAddressInline, LegalDateAdmin


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_initials",
        "user_email",
        "user_phone",
        "created_at",
        "order_type",
        "order_face",
        "order_paymant",
        "order_status",
        "show_total_price",
    )
    list_filter = (
        "order_type",
        "order_status",
    )
    list_display_links = ("id", "user_initials")
    list_per_page = 40
    list_max_show_all = 300

    date_hierarchy = "created_at"
    filter_horizontal = ["order_additionalservices"]
    search_fields = ("id", "user_email", "user_phone", "user_initials")
    empty_value_display = "-"
    list_editable = ("order_status", "order_paymant")
    list_select_related = ("product_info", "items")
    inlines = [OrderItemsInline, OrderAddressInline, LegalDateAdmin]

    # Подсчет общей стоимости заказа
    def show_total_price(self, obj):
        total = obj.total_cost()
        return f"{total} руб."

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related(
                "order_type",
                "order_face",
                "order_status",
                "payment_type",
            )
        )


class AdressAdmin(admin.ModelAdmin):
    list_display = ("city", "region")
