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
        "cost",
        "count",
        "rating",
        "description",
        "subcatalog",
        "created_at",
        "promotion",
        "promotion_cost",
    )
    list_filter = ("subcatalog", "promotion")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin View for Order"""

    list_display = (
        "order_number",
        "user",
        "created_at",
        "order_type",
        "order_status",
        "order_address",
        "get_products_display",
        "get_total_cost",
    )
    list_filter = ("order_type", "order_status")

    def get_products_display(self, obj):
        products_data = obj.products
        products_display = ""
        for product in products_data:
            product_id = product.get("product_id")
            quantity = product.get("quantity")
            try:
                product_name = Product.objects.get(id=product_id).name
                products_display += (
                    f"{product_name} (ID: {product_id}), Количество: {quantity}\n"
                )
            except Product.DoesNotExist:
                products_display += f"ID: {product_id}, Количество: {quantity}\n"
        return products_display

    get_products_display.short_description = "Товары"

    def get_total_cost(self, obj):
        products_data = obj.products
        total_cost = 0
        for product in products_data:
            product_id = product.get("product_id")
            quantity = product.get("quantity")
            try:
                product_cost = Product.objects.get(id=product_id).cost
                total_cost += product_cost * quantity
            except Product.DoesNotExist:
                pass
        return total_cost

    get_total_cost.short_description = "Общая стоимость"
