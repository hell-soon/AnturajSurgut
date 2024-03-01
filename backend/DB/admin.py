from django.contrib import admin
from .models import *


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image")


@admin.register(SubCatalog)
class SubCatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "catalog", "name", "image")
    search_fields = ["id_1C"]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class ProductInfoInline(admin.TabularInline):
    model = ProductInfo
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    inlines = [ProductInfoInline]
    list_filter = ("sub_catalog", "rating")
    search_fields = ["name"]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInfo)
