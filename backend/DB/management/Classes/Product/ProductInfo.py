from DB.models import ProductInfo
import random


class ProductInfoCreator:
    def create(self, products, colors, sizes):
        for product in products:
            # Получение всех цветов и размеров
            for _ in range(
                random.randint(1, 5)
            ):  # Создаем от 1 до 5 экземпляров ProductInfo
                color = random.choice(colors)
                size = random.choice(sizes)
                quantity = random.randint(1, 100)  # Количество от 1 до 100
                cost = round(
                    random.uniform(100, 10000), 2
                )  # Цена от 100 до 1000 с округлением до 2 знаков после запятой
                promotion = random.choice([True, False])  # Рандомное определение акции
                promotion_cost = (
                    round(cost * 0.8, 2) if promotion else None
                )  # Цена со скидкой 20%

                product_info = ProductInfo(
                    product=product,
                    color=color,
                    size=size,
                    quantity=quantity,
                    cost=cost,
                    promotion=promotion,
                    promotion_cost=promotion_cost,
                )
                product_info.save()
