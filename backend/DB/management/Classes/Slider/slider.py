from sitedb.models import Slider
from django.conf import settings
from DB.management.Utils.random_images import set_rangom_image

slider_text = [
    "Вышивка на текстиле любой сложности",
    "Школьная форма в наличии и под заказ",
    "Индивидуальный пошив одежды и текстиля для дома и офиса",
    "Текстиль для дома, гостиниц и отелей",
    "Антураж лучший магазин",
]


class SliderCreator:
    def __init__(self, dir):
        self.dir = dir

    def create(self):
        sliders = []
        for i in range(5):
            slider = Slider(
                title=f"Тестовый слайдер {i}",
                text=slider_text[i],
                url=settings.SITE_URL,
                is_active=True,
            )
            sliders.append(slider)

        data = Slider.objects.bulk_create(sliders)
        set_rangom_image(self.dir, data)
