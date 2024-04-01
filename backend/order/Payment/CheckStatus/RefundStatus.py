from celery import shared_task

from yookassa.payment import Payment
from yookassa.configuration import Configuration
from django.conf import settings


Configuration.account_id = settings.YOOKASSA_ACCOUNT_ID
Configuration.secret_key = settings.YOOKASSA_SECRET


@shared_task
def check_payment_refund(payment_id, order_number):
    pass
