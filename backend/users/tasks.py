from celery import shared_task
from users.models import CustomUser
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


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
