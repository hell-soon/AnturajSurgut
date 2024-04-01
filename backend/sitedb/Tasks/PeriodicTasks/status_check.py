from celery import shared_task
from sitedb.models import Sertificate

from django.utils import timezone


@shared_task
def status_check():
    print("ВОРК ВОРК")
    for sertificate in Sertificate.objects.all():
        if sertificate.end_date < timezone.now():
            sertificate.status = False
            sertificate.save()

        if sertificate.quanity == 0:
            sertificate.status = False
            sertificate.save()
