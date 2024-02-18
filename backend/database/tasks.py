from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order
from django.contrib.auth.models import Group


@shared_task
def send_html_email(subject, template_name, data, recipient_list):
    html_content = render_to_string(template_name, data)
    msg = EmailMultiAlternatives(subject, "", settings.EMAIL_HOST_USER, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
def send_order_confirmation_email(contact_info, order_number):
    recipient_list = [contact_info]
    order = Order.objects.get(order_number=order_number)
    data = {
        "initials": order.user_initials,
        "order_number": order.order_number,
        "order_address": order.order_address,
        "order_status": order.order_status,
        "order_comment": order.comment,
        "order_paymant": order.order_paymant,
    }
    send_html_email(
        "Ваш заказ принят в работу",
        "database/email/email_for_user_order.html",
        data,
        recipient_list,
    )


@shared_task
def send_email_for_manager(contact_info, order_number):
    recipient_list = Group.objects.get(name="Менеджеры").user_set.all()
    order = Order.objects.get(order_number=order_number)
    data = {
        "id": order.id,
        "initials": order.user_initials,
        "user_contact": [contact_info],
        "order_number": order.order_number,
        "order_address": order.order_address,
        "order_status": order.order_status,
        "order_comment": order.comment,
    }
    send_html_email(
        "Заказ от Юридического лица",
        "database/email/email_for_managers.html",
        data,
        recipient_list,
    )


@shared_task
def send_email_for_track_number(contact_info, order_number, track_number):
    recipient_list = [contact_info]
    order = Order.objects.get(order_number=order_number)
    data = {
        "initials": order.user_initials,
        "order_number": order.order_number,
        "order_address": order.order_address,
        "order_status": order.order_status,
        "track_number": track_number,
    }
    send_html_email(
        "Ваш заказ", "database/email/email_for_track_number.html", data, recipient_list
    )
