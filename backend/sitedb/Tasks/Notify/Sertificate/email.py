from django.conf import settings
from django.contrib.auth.models import Group

from celery import shared_task

from DB.Tasks.Email.send_html import send_html_email


@shared_task
def send_sertificate_email(instance):
    template_name = "email/sertificate.html"
    recipient_list = Group.objects.get(name="Подписчики").user_set.all()
    data = {
        "code": instance.code,
        "quanity": instance.quanity,
        "end_date": instance.end_date,
        "site_url": settings.SITE_URL,
        "discount": instance.discount,
    }
    send_html_email(
        "В Антураж появился новый сертификат", template_name, data, recipient_list
    )
