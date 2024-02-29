import random
from DB.models import Product


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
                product.save()
                # Присвоение тэгов
                product.tags.set(random.sample(tags, random.randint(1, len(tags))))
                products.append(product)
        return products
