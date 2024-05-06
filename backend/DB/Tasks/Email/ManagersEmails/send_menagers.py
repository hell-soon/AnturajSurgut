from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import Group
from order.models import Order
from ..send_html import send_html_email


@shared_task
def send_email_for_manager(pk: int):
    group, _ = Group.objects.get_or_create(name="Менеджеры")
    recipient_list = group.user_set.all()
    order = Order.objects.get(pk=pk)
    url = f"{settings.SITE_URL}/admin/order/order/{order.id}/change/"
    data = {
        "id": order.id,
        "initials": order.user_initials,
        "user_email": order.user_email,
        "user_phone": order.user_phone,
        "order_number": order.id,
        "order_status": order.get_status_name(),
        "order_comment": order.comment,
        "site_url": url,
    }
    if recipient_list:
        send_html_email(
            "Заказ от Юридического лица",
            "DB/email/email_for_managers.html",
            data,
            recipient_list,
        )
