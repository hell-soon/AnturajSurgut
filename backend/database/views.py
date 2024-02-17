from django.utils.text import slugify
from .models import Catalog, SubCatalog, Size, Product, ProductImage, Tags
import random
from django.shortcuts import render
from django.http import HttpResponse


def random_product_name():
    word_list = [
        "Футболка",
        "Джинсы",
        "Платье",
        "Куртка",
        "Сапоги",
        "Шляпа",
        "Рубашка",
        "Шарф",
        "Пиджак",
        "Шорты",
    ]
    return " ".join(random.choices(word_list, k=random.randint(1, 2)))


def create_products(request):
    catalogs = ["Школьная форма", "Одежда", "Верхняя одежда", "Обувь"]
    subcatalogs = {
        "Школьная форма": ["Школьные платья", "Школьные брюки", "Школьные рубашки"],
        "Одежда": ["Футболки", "Джинсы", "Платья"],
        "Верхняя одежда": ["Пальто", "Куртки", "Пуховики"],
        "Обувь": ["Кроссовки", "Сапоги", "Туфли"],
    }

    for catalog_name in catalogs:
        catalog = Catalog.objects.create(name=catalog_name)

        for subcatalog_name in subcatalogs[catalog_name]:
            subcatalog = SubCatalog.objects.create(
                name=subcatalog_name, catalog=catalog
            )

            for i in range(1, 4):  # Создаем 3 товара для каждого подкаталога
                product = Product.objects.create(
                    name=random_product_name(),
                    cost=random.uniform(1000, 10000),
                    count=random.randint(0, 500),
                    rating=random.randint(0, 150),
                    description=f"Description for Product {i} in {subcatalog_name}",
                    subcatalog=subcatalog,  # Указываем связанный подкаталог
                    promotion=random.choice([True, False]),
                    promotion_cost=(
                        random.uniform(1000, 5000)
                        if random.choice([True, False])
                        else None
                    ),
                )

                # Добавляем случайные размеры, изображения и тэги к товару
                sizes = Size.objects.order_by("?")[: random.randint(1, 3)]
                product.size.add(*sizes)

                images = ProductImage.objects.order_by("?")[: random.randint(1, 3)]
                product.image.add(*images)

                tags = Tags.objects.order_by("?")[: random.randint(1, 3)]
                product.tags.add(*tags)

    return HttpResponse("Products created successfully")
