from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    Catalog,
    SubCatalog,
    Product,
    Size,
    ProductImage,
    Tags,
    Favorite,
    Cart,
    CartItem,
)


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


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
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


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Admin View for Cart"""

    list_display = ("user", "total_cost")


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """Admin View for CartItem"""

    list_display = ("product", "quantity", "cart", "subtotal")
    list_filter = ("cart",)
