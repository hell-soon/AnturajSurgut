from celery import shared_task
from django.conf import settings
from order.models import Order
from yookassa.payment import Payment
from yookassa.configuration import Configuration
from django.http import HttpResponse
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from icecream import ic


Configuration.account_id = settings.YOOKASSA_ACCOUNT_ID
Configuration.secret_key = settings.YOOKASSA_SECRET


@shared_task()
def check_payment_status(payment_id, order_number):
    print(payment_id, order_number)
    from time import sleep
    from celery import chain

    while True:
        payment_id = payment_id
        payment = Payment.find_one(payment_id)
        if payment.status == "succeeded":
            order = Order.objects.get(order_number=order_number)
            order.order_paymant = True
            order.save()
            break
        else:
            print(f"Статус заказа {order_number} не изменился")
            sleep(60)  # ожидать 60 секунд (1 минуту)
