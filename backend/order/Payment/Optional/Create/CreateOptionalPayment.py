import uuid
import logging

from django.conf import settings
from order.models import Order, OrderItems
from yookassa.configuration import Configuration
from yookassa.payment import Payment
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...CheckStatus.PaymentStatus import check_payment_status

Configuration.account_id = settings.YOOKASSA_ACCOUNT_ID
Configuration.secret_key = settings.YOOKASSA_SECRET

logger = logging.getLogger("payment_create")


@api_view(["POST"])
def create_peyment(request, order_number):
    order = Order.objects.get(order_number=order_number)
    if order.order_paymant == False:
        payment = create_object(order_number)

        if payment.id:
            payment_id = payment["id"]
            check_payment_status.delay(payment_id, order_number)
        else:
            return Response(
                {"message": "Не удалось создать платеж, повторите попытку позже"}
            )
    else:
        payment = "Заказ уже оплачен"
    return Response({"message": payment})


@api_view(["POST"])
def check_payment(request, payment_id):
    payment = Payment.find_one(payment_id)
    return Response({"message": payment.status})


def create_object(order_number):
    """
    Функция создает тело платежа, принимает аргументы order_number

    param order_number: str
    return: Payment: object
    """

    order_cost = 0
    service_cost = 0
    product_cost = 0
    try:
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
    except Order.DoesNotExist:
        logger.error(f"Order does not exist- {order_number}")
        return None
    except OrderItems.DoesNotExist:
        logger.error(f"OrderItems does not exist- {order_number}")
        return None
    except Exception as e:
        logger.error(e)
        return None
