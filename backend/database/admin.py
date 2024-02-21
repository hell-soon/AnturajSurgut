from django.contrib import admin
from django.utils.safestring import mark_safe
import json
from .models import (
    Catalog,
    SubCatalog,
    Product,
    Size,
    Tags,
    Order,
    Additionalservices,
    OrderItems,
)
from allauth.account.models import EmailAddress


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("name", "image")


@admin.register(SubCatalog)
class Admin(admin.ModelAdmin):
    list_display = ("name", "image")
    search_fields = ("name", "catalog__name")


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
        "get_cost",
        "count",
        "rating",
        "description",
        "subcatalog",
        "created_at",
        "promotion",
        "get_promotion_cost",
    )
    list_filter = ("subcatalog", "promotion")
    search_fields = ("name", "description", "id")

    def get_cost(self, obj):
        return f"{round(obj.cost, 2)} Рублей"

    get_cost.short_description = "Цена"

    def get_promotion_cost(self, obj):
        if obj.promotion_cost is not None:
            return f"{round(obj.promotion_cost, 2)} Рублей"
        else:
            return None

    get_promotion_cost.short_description = "Цена по акции"


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
