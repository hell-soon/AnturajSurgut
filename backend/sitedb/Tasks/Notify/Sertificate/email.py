from DB.Tasks.Email.Send.send_html import send_html_email
from celery import shared_task
from django.contrib.auth.models import Group


@shared_task
def send_sertificate_email(instance):
    template_name = "email/sertificate.html"
    recipient_list = Group.objects.get(name="Подписчики").user_set.all()
    data = {
        "certificate": instance.code,
        "end_date": instance.end_date,
        "quanity": instance.quanity,
    }
    send_html_email(
        "В Антураж появился новый сертификат", template_name, data, recipient_list
    )
