from django.db.models.signals import post_save
from django.dispatch import receiver

from order.models import Order

from DB.Tasks.Email.TypesEmail.Managers.send_menagers import (
    send_email_for_manager,
)
from DB.Tasks.Email.TypesEmail.Order.confirm_email import (
    send_order_confirmation_email,
)
from DB.Tasks.Sms.send_sms import send_sms_to_user
from icecream import ic


@receiver(post_save, sender=Order)
def send_email_order(sender, instance, created, **kwargs):
    """
    Сигнал который отрабатывает при создании нового заказа.
    Отправляет письмо менеджерам если заказ пришел от Юридического лица
    Отправляет клиенту письмо на указанный email или Смс на телефон с номером заказа
    """
    if created:
        if instance.order_face.name == "Юридическое лицо":
            send_email_for_manager.delay(instance.order_number)
        else:
            pass
        if instance.user_email:
            send_order_confirmation_email.delay(instance.order_number)
        else:
            sms_text = f"Спасибо за заказ в Антураж.\n Номер вашего заказа: {instance.order_number}"
            send_sms_to_user.delay(instance.user_phone, sms_text)
