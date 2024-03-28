import uuid
from django.apps import apps
from django.db.utils import IntegrityError


def generate_order_number():
    Order = apps.get_model("order", "Order")  # Получаем модель Order

    while True:
        order_number = str(uuid.uuid4())[:10]
        try:
            existing_order = Order.objects.get(order_number=order_number)
            if existing_order:
                continue
        except Order.DoesNotExist:
            return order_number
        except IntegrityError:
            pass
