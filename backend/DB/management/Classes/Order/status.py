from order.models import OrderStatus


class StatusCreator:
    def create(self, order_settings):
        status = [
            OrderStatus(settings=order_settings, name="Не готов"),
            OrderStatus(settings=order_settings, name="Готов к выдаче"),
            OrderStatus(settings=order_settings, name="Передан в доставку"),
            OrderStatus(settings=order_settings, name="Доставлен"),
            OrderStatus(settings=order_settings, name="Отменен"),
            OrderStatus(settings=order_settings, name="Завершен"),
        ]
        OrderStatus.objects.bulk_create(status)
