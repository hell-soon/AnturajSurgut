import uuid
from django.conf import settings


from yookassa.configuration import Configuration
from django.conf import settings


Configuration.account_id = settings.YOOKASSA_ACCOUNT_ID
Configuration.secret_key = settings.YOOKASSA_SECRET


def payment_notyfication(request):
    pass