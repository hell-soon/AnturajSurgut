from celery import shared_task
from django.contrib.auth.models import Group
from ..send_html import send_html_email

from icecream import ic


@shared_task
def send_error_for_manager(result: dict, phone: str):
    if result.get(phone, {}).get("status", False):
        pass
    else:
        sms_id = result.get(phone, {}).get("sms_id")
        error_message = result.get(phone, {}).get("status_text")
        group, _ = Group.objects.get_or_create(name="Менеджеры")
        recipient_list = group.user_set.all()
        ic(recipient_list)
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
