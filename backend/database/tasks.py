from celery import shared_task


@shared_task
def send_order_confirmation_email(contact_info):
    print("Sending email to: " + contact_info)


@shared_task
def send_email_for_manager(contact_info):
    pass


@shared_task
def send_email_for_track_number(contact_info, track_number):
    print("Sending email to: " + contact_info)
    print("Track number: " + track_number)
