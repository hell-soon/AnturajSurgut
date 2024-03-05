from DB.models import Catalog


class CatalogsCreator:
    def create(self):
        catalogs = [
            Catalog(name="Одежда"),
            Catalog(name="Обувь"),
            Catalog(name="Товары для дома"),
            Catalog(name="Интерьер"),
            Catalog(name="Школьная фомра"),
            Catalog(name="Подарки"),
            Catalog(name="Ткани"),
            Catalog(name="Фурнитура"),
            Catalog(name="Текстиль"),
        ]
        Catalog.objects.bulk_create(catalogs)
        return catalogs
