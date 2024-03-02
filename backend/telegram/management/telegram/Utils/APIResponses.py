import requests
from .AdditionInfo import addition_info_for_product
from .OrderInfo import order_info
from urllib.parse import quote


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


# Список каталогов
def get_catalog_list(bot, API_URL):
    response = requests.get(f"{API_URL}list/catalog/")
    catalogs = response.json()
    return catalogs


# Список подкаталогов
def get_subcatalog_list(bot, API_URL, catalog_id):
    response = requests.get(f"{API_URL}list/subcatalog/?catalog_id={catalog_id}")
    subcatalogs = response.json()
    return subcatalogs


# Список продуктов
def get_product_for_subcatalog(bot, API_URL, subcatalog_id):
    response = requests.get(f"{API_URL}list/product/?sub_catalog={subcatalog_id}")
    products = response.json()
    return products


# Список заказов
def get_order(bot, API_URL, params):
    response = requests.get(f"{API_URL}list/order", params=params)
    orders = response.json()
    return orders


# Информация о заказе
def get_order_info(API_URL, order_number):
    response = requests.get(f"{API_URL}list/order-info/{order_number}/")
    order = response.json()
    text = order_info(order)
    return text
