from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


@shared_task
def send_html_email(subject: str, template_name: str, data: dict, recipient_list: list):
    html_content = render_to_string(template_name, data)
    msg = EmailMultiAlternatives(subject, "", settings.EMAIL_HOST_USER, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
