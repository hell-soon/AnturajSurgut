from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from order.models import Order
from django.contrib.auth.models import Group
from smsru.service import SmsRuApi
from DB.utils.codes import STATUS_MAP


@shared_task
def send_html_email(subject, template_name, data, recipient_list):
    html_content = render_to_string(template_name, data)
    msg = EmailMultiAlternatives(subject, "", settings.EMAIL_HOST_USER, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
def send_order_confirmation_email(order_number):
    order = Order.objects.get(order_number=order_number)
    recipient_list = [order.user_email]
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
        "DB/email/email_for_user_order.html",
        data,
        recipient_list,
    )


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


@shared_task
def send_email_for_track_number(order_number, track_number):
    order = Order.objects.get(order_number=order_number)
    recipient_list = [order.user_email]
    data = {
        "initials": order.user_initials,
        "order_number": order.order_number,
        "order_address": order.order_address,
        "order_status": order.order_status,
        "track_number": track_number,
    }
    send_html_email(
        "Ваш заказ", "DB/email/email_for_track_number.html", data, recipient_list
    )


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


@shared_task
def send_error_for_manager(result, phone):
    if result.get(phone, {}).get("status", False):
        pass
    else:
        sms_id = result.get(phone, {}).get("sms_id")
        error_message = result.get(phone, {}).get("status_text")
        recipient_list = Group.objects.get(name="Менеджеры").user_set.all()
        data = {
            "id": sms_id,
            "phone": phone,
            "error_message": error_message,
        }
        send_html_email(
            "Ошбика при отправке смс",
            "DB/email/error_email_for_manager.html",
            data,
            recipient_list,
        )


@shared_task
def send_sms_to_user(user_phone, sms_text):
    sms = SmsRuApi()
    phone = sms.beautify_phone(user_phone)
    result = sms.send_one_sms(phone, sms_text)
    send_error_for_manager.delay(result, phone)
