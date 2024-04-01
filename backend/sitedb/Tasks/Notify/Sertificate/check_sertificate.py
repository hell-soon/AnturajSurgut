from celery import shared_task
from django.db.models import Q
from sitedb.models import Sertificate
from django.utils import timezone


# TODO FIX
@shared_task
def test():
    current_date = timezone.now()
    Sertificate.objects.filter(
        Q(status=True) & (Q(quanity__lte=0) | Q(end_date__lt=current_date))
    ).update(status=False)
