from order.models import OrderType


class OrderTypeCreator:
    def create(self, order_settings):
        order_type = [
            OrderType(settings=order_settings, name="Самовывоз"),
            OrderType(settings=order_settings, name="Доставка до двери"),
            OrderType(settings=order_settings, name="Доставка транспортной компанией"),
        ]
        OrderType.objects.bulk_create(order_type)
        return order_type
