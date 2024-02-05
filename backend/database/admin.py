from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Catalog, SubCatalog, Product, Size, ProductImage, Value, Tags


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


@admin.register(SubCatalog)
class Admin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name', 'catalog__name')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'value', 'count', 'rating', 'description', 'subcatalog', 'created_at', 'promotion', 'promotion_cost')
    list_filter = ('subcatalog', 'value', 'promotion')


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)
