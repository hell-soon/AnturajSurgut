from django.core.files import File
from sitedb.models import (
    Contact,
    SocialAccount,
    Address,
    Requisites,
    WokrTime,
    SiteInfo,
)


class InfoSiteCreator:
    def create_pk(self):
        data = SiteInfo.objects.create(name="Текстиль Антураж")
        return data

    def create_contact(self, data):
        Contact.objects.create(
            info=data,
            email="uytopt@yandex.ru",
            phone="8 (346) 221-44-40",
            fax="(3462) 582321",
        )
        Address.objects.create(
            info=data,
            address="628401, РФ, Тюменская область, ХМАО, г. Сургут, ул. И. Каролинского 13, вход со стороны дороги магазин «Галерея Текстиля Антураж»",
            longitude=73.447445,
            latitude=61.254702,
        )
        Requisites.objects.create(
            info=data,
            ip="ИП Соловьева Алёна Анатольевна",
            inn="ИНН 860222328184",
            legal_address="Юридический адрес: 628415, РФ, Тюменская область, ХМАО, г. Сургут, ул. Приозерная, д. 3/1",
        )
        WokrTime.objects.create(
            info=data,
            work_time="с 10:00 до 18:00, без выходных (перерыв с 12:30 до 13:30)",
        )

    def create_social(self, data):
        social = [
            SocialAccount(
                info=data,
                name="ВКонтакте",
                url="https://vk.com/anturazh_surgut",
                icon=File(open("media/TestInfoSite/vk.png", "rb")),
            ),
            SocialAccount(
                info=data,
                name="Телеграмм",
                url="https://t.me/AnturajBot",
                icon=File(open("media/TestInfoSite/tg.png", "rb")),
            ),
        ]
        SocialAccount.objects.bulk_create(social)
