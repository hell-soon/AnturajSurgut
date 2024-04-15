import random
from DB.models import Product, ProductImage
from django.db import transaction


class ProductCreator:
    def create(self, sub_catalogs, tags):
        products = []
        for sub_catalog in sub_catalogs:
            for i in range(5):  # Создаем 5 продуктов для каждого подкаталога
                product_name = f"{sub_catalog.name} {i+1}"
                product = Product(
                    name=product_name,
                    description=f"Описание для продукта {product_name}",
                    sub_catalog=sub_catalog,
                )
                products.append(product)

        # Используем bulk_create для создания всех объектов за один раз
        with transaction.atomic():
            created_products = Product.objects.bulk_create(products)

        # Присвоение тэгов после сохранения объектов
        for product in created_products:
            product.tags.set(random.sample(tags, random.randint(1, 7)))

        # Присвоение случайных изображений после сохранения объектов
        all_images = list(ProductImage.objects.all())
        for product in created_products:
            random_images = random.sample(all_images, 10)
            for image in random_images:
                product.image.add(image)

        return created_products
