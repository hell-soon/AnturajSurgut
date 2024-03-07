import uuid
from django.conf import settings
from yookassa.refund import Refund
from yookassa.configuration import Configuration
from yookassa.payment import Payment
from django.conf import settings

from order.models import Order, OrderItems
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from icecream import ic
from rest_framework.response import Response
from django.http import JsonResponse
from ..Create.CreateOptionalPayment import create_object

Configuration.account_id = settings.YOOKASSA_ACCOUNT_ID
Configuration.secret_key = settings.YOOKASSA_SECRET


@api_view(["POST"])
def refund_payment(order_number):
    ic(order_number)
    payment_id = "2d7a96c9-000f-5000-8000-1fc74481e025"
    payment = create_object(order_number)
    ic(payment)
    refund = Refund.create(
        {
            "amount": {"value": "213.00", "currency": "RUB"},
            "payment_id": payment_id,
        }
    )
    return Response(refund)


def test(order_number):
    order_cost = 0
    service_cost = 0
    product_cost = 0
    order = Order.objects.get(order_number=order_number)
    items = OrderItems.objects.filter(order=order)

    # Цена всех товаров
    for item in items:
        product_cost += item.total_cost
    # Цена доп услуг
    for service in order.order_additionalservices.all():
        service_cost += service.cost
    order_cost += product_cost + service_cost
    payment = Payment.create(
        {
            "amount": {"value": order_cost, "currency": "RUB"},
            "confirmation": {
                "type": "redirect",
                "return_url": "https://www.example.com/return_url",
            },
            "capture": True,
            "description": f"Оплата заказа {order_number}",
        },
        uuid.uuid4(),
    )
    return payment
