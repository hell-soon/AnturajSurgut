import requests
from .AdditionInfo import addition_info_for_product


# Популярные товары
def get_popular_product(popular_product, API_URL):
    response = requests.get(f"{API_URL}list/product/?high_rating=True")
    product = response.json()
    for item in product:
        popular_product.append(item["product"]["id"])

    return popular_product


# Информация о товаре
def get_product(product_id, API_URL):
    response = requests.get(f"{API_URL}list/product/{product_id}")
    return response.json()


# Список дополнительной информации(Размер цвет цена и тд)
def get_addition_info_for_product(value, API_URL):
    response = requests.get(f"{API_URL}list/product/info/{value}")
    data = response.json()
    text = addition_info_for_product(data)
    return text
