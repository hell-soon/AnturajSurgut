from celery import shared_task
from django.contrib.auth.models import Group
from ....Send.send_html import send_html_email


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
