import uuid
from django.conf import settings


from yookassa.payment import Payment
from yookassa.configuration import Configuration
from django.conf import settings


Configuration.account_id = settings.YOOKASSA_ACCOUNT_ID
Configuration.secret_key = settings.YOOKASSA_SECRET


def create_online_check(order):
    total_cost = order.total_cost()
    text = f"Оплата заказа {order.order_number}.\nСпасибо за покупку в Антураж!"
    payment = Payment.create(
        {
            "amount": {"value": total_cost, "currency": "RUB"},
            "confirmation": {
                "type": "redirect",
                "return_url": settings.SITE_URL,
            },
            "capture": True,
            "description": text,
        },
        uuid.uuid4(),
    )
    return payment
