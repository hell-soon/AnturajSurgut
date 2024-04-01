from celery import shared_task
from order.models import Order
from DB.utils.codes import STATUS_MAP
from .....Send.send_html import send_html_email


@shared_task
def send_email_for_change_order_status(order_number, order_status):
    order = Order.objects.get(order_number=order_number)
    recipient_list = [order.user_email]
    status_name = STATUS_MAP.get(order_status)
    data = {
        "initials": order.user_initials,
        "order_number": order.order_number,
        "order_address": order.order_address,
        "order_status": status_name,
        "created_at": order.created_at,
    }
    send_html_email(
        "Изменение статуса заказа",
        "DB/email/email_for_change_order_status.html",
        data,
        recipient_list,
    )
