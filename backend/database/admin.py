from django.contrib import admin
from django.utils.safestring import mark_safe
import json
from .models import Catalog, SubCatalog, Product, Size, Tags, Order, Additionalservices
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
        "get_products_display",
        "order_face",
        "get_additional_services",
        "get_total_cost",
        "order_paymant",
        "order_status",
        "comment",
        "track_number",
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
                    f"{product_name} (ID: {product_id}) - Количество: {quantity},\n"
                )
            except Product.DoesNotExist:
                products_display += f"ID: {product_id}, Количество: {quantity}\n"
        return products_display

    get_products_display.short_description = "Товары"

    def get_total_cost(self, obj):
        total_cost = 0
        for product_data in obj.products:
            product_id = product_data.get("product_id")
            quantity = product_data.get("quantity")
            try:
                product = Product.objects.get(id=product_id)
                if product.promotion and product.promotion_cost:
                    total_cost += product.promotion_cost * quantity
                else:
                    total_cost += product.cost * quantity
            except Product.DoesNotExist:
                pass

        # Добавляем стоимость дополнительных услуг
        for service in obj.order_additionalservices.all():
            total_cost += service.price

        return round(total_cost, 2)

    get_total_cost.short_description = "Общая стоимость (В Рублях)"

    def get_additional_services(self, obj):
        additional_services = obj.order_additionalservices.all()
        if additional_services:
            return ", ".join([str(service) for service in additional_services])
        else:
            return "Нету дополнительных услуг"

    get_additional_services.short_description = "Дополнительные услуги"
