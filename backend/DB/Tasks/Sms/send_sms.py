from celery import shared_task

from smsru.service import SmsRuApi
from ..Email.TypesEmail.Managers.Errors.sms_error import send_error_for_manager


@shared_task
def send_sms_to_user(user_phone, sms_text):
    sms = SmsRuApi()
    phone = sms.beautify_phone(user_phone)
    result = sms.send_one_sms(phone, sms_text)
    send_error_for_manager.delay(result, phone)
