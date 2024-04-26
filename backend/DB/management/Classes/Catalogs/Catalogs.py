import os
import random

from django.core.files import File

from DB.models import Catalog
from DB.management.Utils.random_images import set_rangom_image


class CatalogsCreator:
    def __init__(self, dir):
        self.dir = dir

    def create(self):
        catalogs = [
            Catalog(name="Одежда"),
            Catalog(name="Обувь"),
            Catalog(name="Товары для дома"),
            Catalog(name="Интерьер"),
            Catalog(name="Школьная форма"),
            Catalog(name="Подарки"),
            Catalog(name="Ткани"),
            Catalog(name="Фурнитура"),
            Catalog(name="Текстиль"),
        ]
        data = Catalog.objects.bulk_create(catalogs)
        set_rangom_image(self.dir, data)
        return catalogs
