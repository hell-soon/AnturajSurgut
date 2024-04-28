from django.shortcuts import render
from django.conf import settings

from sitedb.models import Sertificate


def test(request):
    sertificate = Sertificate.objects.all().first()
    data = {
        "code": sertificate.code,
        "quanity": sertificate.quanity,
        "end_date": sertificate.end_date,
        "site_url": settings.SITE_URL,
        "discount": sertificate.discount,
    }
    return render(request, "email/sertificate.html", data)
