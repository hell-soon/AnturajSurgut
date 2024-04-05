from django.core.files import File
from sitedb.models import Contact, SocialAccount


class InfoSiteCreator:
    def create_contact(self):
        Contact.objects.create(
            email="uytopt@yandex.ru", phone="8 (346) 221-44-40", fax="(3462) 582321"
        )

    def create_social(self):
        social = [
            SocialAccount(
                name="ВКонтакте",
                url="https://vk.com/anturazh_surgut",
                icon=File(open("media/TestInfoSite/vk.png", "rb")),
            ),
            SocialAccount(
                name="Телеграмм",
                url="https://t.me/AnturajBot",
                icon=File(open("media/TestInfoSite/tg.png", "rb")),
            ),
        ]
        SocialAccount.objects.bulk_create(social)
