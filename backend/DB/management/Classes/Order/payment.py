from order.models import PaymentType


class PaymentTypeCreator:
    def create(self, order_settings):
        order_pay = [
            PaymentType(settings=order_settings, name="Онлайн оплата"),
            PaymentType(settings=order_settings, name="При получении"),
        ]
        PaymentType.objects.bulk_create(order_pay)
        return order_pay
