from django.contrib import admin
from django.utils.html import format_html
from DB.models import ProductInfo
from ..ProductInline.inline import ProductInfoInline
from ....Setup.forms.ProductAdminForm.ProductForm import ProductAdminForm


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

    def change_product_status_action(self, request, queryset):
        for product in queryset:
            if product.product_status:
                product.product_status = False
            else:
                product.product_status = True
            product.save()

    def show_image(self, obj):
        if obj.image.exists():
            image = obj.image.first()
            return format_html('<img src="{}" width="75" height="75" />'.format(image))
        else:
            return None

    # Short description
    show_image.short_description = "Изображение"
    change_product_status_action.short_description = "Изменить статус"
    info_total_quanity_action.short_description = "Информация о количестве"
