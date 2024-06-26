from celery import shared_task
from order.models import Order, OrderAddress
from ..send_html import send_html_email


@shared_task
def send_email_for_track_number(pk: int, track_number: str):
    order = Order.objects.get(pk=pk)
    address = OrderAddress.objects.get(order=order).__str__()
    recipient_list = [order.user_email]
    data = {
        "initials": order.user_initials,
        "order_number": order.id,
        "order_address": address,
        "order_status": order.order_status.name,
        "track_number": track_number,
    }
    send_html_email(
        "Ваш заказ", "DB/email/email_for_track_number.html", data, recipient_list
    )
