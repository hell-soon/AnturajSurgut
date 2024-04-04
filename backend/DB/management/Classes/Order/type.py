from order.models import OrderType


class OrderTypeCreator:
    def create(self):
        order_type = [
            OrderType(name="Самовывоз"),
            OrderType(name="Доставка до двери"),
            OrderType(name="Доставка транспортной компанией"),
        ]
        OrderType.objects.bulk_create(order_type)
        return order_type
