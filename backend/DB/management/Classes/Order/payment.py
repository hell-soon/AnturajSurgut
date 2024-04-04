from order.models import PaymentType


class PaymentTypeCreator:
    def create(self):
        order_pay = [
            PaymentType(name="Онлайн оплата"),
            PaymentType(name="При получении"),
        ]
        PaymentType.objects.bulk_create(order_pay)
        return order_pay
