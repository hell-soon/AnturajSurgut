import os

from celery import shared_task
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from users.models import CustomUser

BASE_URL = os.getenv("BASE_URL")


@shared_task
def welcome_email(user_id):
    user = CustomUser.objects.get(id=user_id)

    data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
    }

    html_content = render_to_string("email/welcome_email.html", data)
    msg = EmailMultiAlternatives(
        "Добро пожаловать в Антураж!",
        "",
        settings.EMAIL_HOST_USER,
        [user.email],
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
def send_link_for_change_pass(email):
    user = CustomUser.objects.get(email=email)
    token = default_token_generator.make_token(user)
    uid64 = urlsafe_base64_encode(force_bytes(user.pk))
    reset_link = f"{BASE_URL}reset-password/{uid64}/{token}/"  # TODO)) ССЫЛКА НА СТРАНИЦУ С ИЗМЕНЕНИМИ ПАРОЛЯ
    data = {
        "reset_link": reset_link,
    }

    html_content = render_to_string("email/reset_password_email.html", data)
    msg = EmailMultiAlternatives(
        "Антураж: Смена пароля",
        "",
        settings.EMAIL_HOST_USER,
        [email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
