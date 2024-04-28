from django.conf import settings
from celery import shared_task
from order.models import Order, OrderAddress
from ..send_html import send_html_email


@shared_task
def send_order_confirmation_email(pk):
    order = Order.objects.get(pk=pk)
    recipient_list = [order.user_email]
    data = {
        "initials": order.user_initials,
        "order_number": order.order_number,
        "order_status": order.order_status.name,
        "order_comment": order.comment,
        "order_paymant": order.order_paymant,
        "site_url": settings.SITE_URL,
    }
    send_html_email(
        "Ваш заказ принят в работу",
        "DB/email/email_for_user_order.html",
        data,
        recipient_list,
    )
