from order.models import OrderStatus


class StatusCreator:
    def create(self):
        status = [
            OrderStatus(name="Не готов"),
            OrderStatus(name="Готов к выдаче"),
            OrderStatus(name="Передан в доставку"),
            OrderStatus(name="Доставлен"),
            OrderStatus(name="Отменен"),
            OrderStatus(name="Завершен"),
        ]
        OrderStatus.objects.bulk_create(status)
