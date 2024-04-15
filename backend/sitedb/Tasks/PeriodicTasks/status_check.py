from celery import shared_task
from sitedb.models import Sertificate
from django.db.models import Q
from django.utils import timezone


@shared_task
def check_sertificate():
    current_date = timezone.now()
    Sertificate.objects.filter(
        Q(status=True) & (Q(quanity__lte=0) | Q(end_date__lt=current_date))
    ).update(status=False)
