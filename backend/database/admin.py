from django.contrib import admin
from django.utils.safestring import mark_safe
import json
from .models import (
    Catalog,
    SubCatalog,
    Product,
    Size,
    Tags,
    Favorite,
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


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Admin View for Favorite"""

    list_display = ("product", "user")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin View for Order"""

    list_display = (
        "user",
        "created_at",
        "order_number",
        "order_type",
        "order_status",
        "order_address",
        "get_products_display",
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

    get_products_display.short_description = "Products"
