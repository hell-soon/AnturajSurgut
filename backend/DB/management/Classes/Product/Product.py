import random
from DB.models import Product, ProductImage
from django.db import transaction


class ProductCreator:
    def create(self, sub_catalogs, tags, compaunds):
        products = []
        for sub_catalog in sub_catalogs:
            for i in range(4):
                product_name = f"{sub_catalog.name} {i+1}"
                product = Product(
                    name=product_name,
                    description=f"Описание для продукта {product_name}",
                    sub_catalog=sub_catalog,
                    rating=random.randint(1, 5),
                )
                products.append(product)

        with transaction.atomic():
            created_products = Product.objects.bulk_create(products)

        for product in created_products:
            product.tags.set(random.sample(tags, random.randint(1, 5)))

        # Присвоение случайных изображений после сохранения объектов
        all_images = list(ProductImage.objects.all())
        for product in created_products:
            random_range = random.randint(1, 10)
            random_images = random.sample(all_images, random_range)
            for image in random_images:
                product.image.add(image)

        for product in created_products:
            product.compound.set(random.sample(compaunds, random.randint(1, 4)))

        return created_products
