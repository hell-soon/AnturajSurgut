from celery import shared_task
from django.contrib.auth.models import Group
from order.models import Order
from ....Send.send_html import send_html_email


@shared_task
def send_email_for_manager(order_number):
    recipient_list = Group.objects.get(name="Менеджеры").user_set.all()
    order = Order.objects.get(order_number=order_number)
    data = {
        "id": order.id,
        "initials": order.user_initials,
        "user_email": order.user_email,
        "user_phone": order.user_phone,
        "order_number": order.order_number,
        "order_address": order.order_address,
        "order_status": order.order_status,
        "order_comment": order.comment,
    }
    send_html_email(
        "Заказ от Юридического лица",
        "DB/email/email_for_managers.html",
        data,
        recipient_list,
    )
