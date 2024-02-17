from celery import shared_task


@shared_task
def send_order_confirmation_email(user_email):
    print("Sending email to: " + user_email)
