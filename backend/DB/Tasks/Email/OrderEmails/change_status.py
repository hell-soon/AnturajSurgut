from celery import shared_task
from order.models import Order, OrderAddress
from ..send_html import send_html_email


@shared_task
def send_email_for_change_order_status(pk: int):
    order = Order.objects.get(pk=pk)
    address = OrderAddress.objects.get(order=order).__str__()
    recipient_list = [order.user_email]
    data = {
        "initials": order.user_initials,
        "order_number": order.id,
        "order_address": address,
        "order_status": order.get_status_name(),
        "created_at": order.created_at,
    }
    send_html_email(
        "Изменение статуса заказа",
        "DB/email/email_for_change_order_status.html",
        data,
        recipient_list,
    )
