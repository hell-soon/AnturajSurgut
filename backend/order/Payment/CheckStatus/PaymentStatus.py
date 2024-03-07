from celery import shared_task
from django.conf import settings
from order.models import Order
from yookassa.payment import Payment
from yookassa.configuration import Configuration
from django.conf import settings


Configuration.account_id = settings.YOOKASSA_ACCOUNT_ID
Configuration.secret_key = settings.YOOKASSA_SECRET

# logger = logging.getLogger(__name__)


@shared_task
def check_payment_status(payment_id, order_number):
    from time import sleep

    try:
        while True:
            payment_id = payment_id
            payment = Payment.find_one(payment_id)
            if payment.status == "succeeded":
                order = Order.objects.get(order_number=order_number)
                order.order_paymant = True
                order.save()
                break
            elif payment.status == "cancelled":
                print("Оплата отменена")
                break
            else:
                sleep(15)
    except Exception as e:
        # logger.error(e)
        print(e)
