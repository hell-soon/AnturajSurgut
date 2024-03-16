from django.contrib import admin
from ..OrderInline.inline import OrderItemsInline
from decimal import Decimal, ROUND_HALF_UP
from order.models import OrderItems
from django.db.models import Sum
import logging


logger = logging.getLogger("AdminPanel")


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_number",
        "user_initials",
        "user_email",
        "user_phone",
        "created_at",
        "order_type",
        "order_face",
        "order_paymant",
        "order_status",
        "show_track",
        "show_total_price",
    )
    list_filter = (
        "order_type",
        "order_status",
    )
    list_display_links = ("order_number", "user_initials")
    list_per_page = 40
    list_max_show_all = 300

    date_hierarchy = "created_at"

    search_fields = (
        "order_number",
        "user_email",
        "user_phone",
        "user_initials",
        "order_address",
    )

    empty_value_display = "-"

    inlines = [OrderItemsInline]

    # Подсчет общей стоимости заказа
    def show_total_price(self, obj):
        if obj:
            try:
                # Используем аннотации для оптимизации запросов к базе данных
                product_cost = (
                    OrderItems.objects.filter(order=obj).aggregate(
                        total_cost=Sum("total_cost")
                    )["total_cost"]
                    or 0
                )
                service_cost = (
                    obj.order_additionalservices.aggregate(cost=Sum("cost"))["cost"]
                    or 0
                )
                order_cost = Decimal(product_cost) + Decimal(service_cost)

                if obj.sertificate:
                    order_cost = order_cost * (Decimal(obj.sertificate.discount) / 100)

                # Округляем до двух знаков после запятой
                order_cost = order_cost.quantize(
                    Decimal("0.01"), rounding=ROUND_HALF_UP
                )

                return f"{order_cost} руб."
            except Exception as e:
                logger.error(e)
                return f"Произошла ошибка"
        else:
            return "Объект заказа не найден."

    # Отображение трэк номера(если есть)
    def show_track(self, obj):
        if obj.track_number:
            return obj.track_number
        else:
            return "-"

    # отображение дополнительных услуг
    def get_additional_services(self, obj):
        additional_services = obj.order_additionalservices.all()
        if additional_services:
            return ", ".join([str(service) for service in additional_services])
        else:
            return "Нету дополнительных услуг"

    get_additional_services.short_description = "Дополнительные услуги"
    show_track.short_description = "Трэк номер"
    show_total_price.short_description = "Общая цена заказа"
