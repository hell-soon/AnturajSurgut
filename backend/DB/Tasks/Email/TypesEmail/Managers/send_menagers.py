from celery import shared_task
from django.contrib.auth.models import Group
from order.models import Order, OrderAddress
from ...Send.send_html import send_html_email


@shared_task
def send_email_for_manager(pk):
    group, _ = Group.objects.get_or_create(name="Менеджеры")
    recipient_list = group.user_set.all()
    order = Order.objects.get(pk=pk)
    address = OrderAddress.objects.get(order=order).__str__()
    data = {
        "id": order.id,
        "initials": order.user_initials,
        "user_email": order.user_email,
        "user_phone": order.user_phone,
        "order_number": order.order_number,
        "order_address": address,
        "order_status": order.order_status,
        "order_comment": order.comment,
    }
    if recipient_list:
        send_html_email(
            "Заказ от Юридического лица",
            "DB/email/email_for_managers.html",
            data,
            recipient_list,
        )
