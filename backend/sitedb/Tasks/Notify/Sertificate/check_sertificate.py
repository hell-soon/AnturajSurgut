import logging
from celery import shared_task
from icecream import ic
from sitedb.models import Sertificate
from django.utils import timezone

logger = logging.getLogger("debug")


@shared_task
def check_sertificate():
    sertificate = Sertificate.objects.filter(status=True)

    for item in sertificate:
        if item.quanity <= 0:
            item.status = False
            item.save()
        else:
            current_date = timezone.now()
            if current_date > item.end_date:
                item.status = False
                item.save()
