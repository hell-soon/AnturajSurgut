from celery import shared_task
from order.models import Order, OrderAddress
from ...Send.send_html import send_html_email


@shared_task
def send_order_confirmation_email(pk):
    order = Order.objects.get(pk=pk)
    address = OrderAddress.objects.get(order=order).__str__()
    recipient_list = [order.user_email]
    data = {
        "initials": order.user_initials,
        "order_number": order.order_number,
        "order_address": address,
        "order_status": order.order_status,
        "order_comment": order.comment,
        "order_paymant": order.order_paymant,
    }
    send_html_email(
        "Ваш заказ принят в работу",
        "DB/email/email_for_user_order.html",
        data,
        recipient_list,
    )
