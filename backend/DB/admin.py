from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.forms import ClearableFileInput

from django import forms
from .Setup.widgets.Preview.ProductPreview import ImageWidget
from .Setup.forms.ProductAdminForm.ProductForm import ProductAdminForm


class SubCatalogAdmin(admin.TabularInline):
    model = SubCatalog
    extra = 0


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image_preview")
    list_display_links = ("id", "name")
    search_fields = ("name", "id")
    inlines = [SubCatalogAdmin]

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="75" height="75" style="object-fit: cover;"/>',
                obj.image.url,
            )
        else:
            return "-"

    image_preview.short_description = "Изображение"


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name", "id")


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview")
    list_display_links = ("id", "image_preview")
    search_fields = ("id",)
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="75" height="75" style="object-fit: cover;"/>',
                obj.image.url,
            )
        else:
            return "Изображение отсутствует"

    image_preview.short_description = "Изображение"


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "color_indicator")
    search_fields = ("name", "id")
    list_display_links = ("id", "name")

    def color_indicator(self, obj):
        return format_html(
            '<div style="background-color: {}; width: 25px; height: 25px; border: 1px solid black"></div>',
            obj.color,
        )

    color_indicator.short_description = "Цвет"


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name", "id")
    list_display_links = ("id", "name")


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class ProductInfoInline(admin.TabularInline):
    model = ProductInfo
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("id", "name", "description", "show_image", "product_status")
    list_display_links = ("name", "id")
    inlines = [ProductInfoInline]
    list_filter = [
        "sub_catalog",
        "product_status",
    ]
    date_hierarchy = "created_at"
    search_fields = ["name", "id"]
    list_per_page = 40
    list_max_show_all = 300
    empty_value_display = "-"
    actions = [
        "change_product_status_action",
        # "info_total_quanity_action",
    ]

    def info_total_quanity_action(self, request, queryset):
        for product in queryset:
            product_info = ProductInfo.objects.filter(product_id=product.id)
            if product_info:
                total_quanity = 0
                for info in product_info:
                    total_quanity += info.quantity
                print(total_quanity)

    info_total_quanity_action.short_description = "Информация о количестве"

    def change_product_status_action(self, request, queryset):
        for product in queryset:
            if product.product_status:
                product.product_status = False
            else:
                product.product_status = True
            product.save()

    change_product_status_action.short_description = "Изменить статус"

    def show_image(self, obj):
        if obj.image.exists():
            image = obj.image.first()
            return format_html('<img src="{}" width="75" height="75" />'.format(image))
        else:
            return None

    show_image.short_description = "Изображение"


admin.site.register(Product, ProductAdmin)
admin.site.site_title = "Антураж"
admin.site.site_header = "Антураж"
