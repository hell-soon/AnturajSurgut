from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import Truncator
from DB.models import ProductInfo
from ..ProductInline.inline import ProductInfoInline
from ....Setup.forms.ProductAdminForm.ProductForm import ProductAdminForm


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = (
        "id",
        "name",
        "show_description",
        "sub_catalog",
        "show_image",
        "product_status",
    )
    list_display_links = (
        "name",
        "id",
    )
    list_select_related = ("sub_catalog",)
    inlines = [ProductInfoInline]
    list_filter = [
        "sub_catalog",
        "product_status",
    ]
    date_hierarchy = "created_at"
    search_fields = ["name", "id"]
    preserve_filters = True
    list_per_page = 40
    list_max_show_all = 300
    empty_value_display = "-"
    actions = [
        "change_product_status_action",
        # "info_total_quanity_action", # TODO
    ]
    filter_horizontal = ("tags", "image")

    def info_total_quanity_action(self, request, queryset):
        for product in queryset:
            product_info = ProductInfo.objects.filter(product_id=product.id)
            if product_info:
                total_quanity = 0
                for info in product_info:
                    total_quanity += info.quantity
                print(total_quanity)

    def change_product_status_action(self, request, queryset):
        for item in queryset:
            if item.product_status:
                item.product_status = False
            else:
                item.product_status = True
            item.save()

    def show_image(self, obj):
        if obj.image.exists():
            image = obj.image.first()
            return format_html(
                '<img src="{}" style="width: 100px; height: 100px; object-fit: cover;" />'.format(
                    image
                )
            )
        else:
            return None

    def show_description(self, obj):
        return format_html(Truncator(obj.description).chars(150))

    # Short description
    show_image.short_description = "Изображение"
    change_product_status_action.short_description = "Изменить статус"
    info_total_quanity_action.short_description = "Информация о количестве"
    show_description.short_description = "Описание"
