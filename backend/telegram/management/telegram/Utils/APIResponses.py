import requests
from .AdditionInfo import addition_info_for_product
from .OrderInfo import order_info


# Основной запрос API
def get_main_product(bot, chat_id, API_URL, product_type, subcatalog_id=None):
    params = {}
    product_ids = []
    if product_type == "popular":
        params = {"high_rating": True}
    elif product_type == "catalog":
        params = {"sub_catalog": subcatalog_id}
    try:
        response = requests.get(f"{API_URL}list/product/", params=params)
        product = response.json()
        for item in product:
            product_ids.append(item["product"]["id"])
        return product_ids
    except requests.exceptions.RequestException as e:
        # Отправляем сообщение об ошибке
        bot.send_message(
            chat_id=chat_id, text="Произошла ошибка сервера, попробуйте позже!"
        )


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
def get_catalog_list(bot, API_URL, chat_id):
    try:
        response = requests.get(f"{API_URL}list/catalog/")
        catalogs = response.json()
        return catalogs
    except requests.exceptions.RequestException as e:
        # Отправляем сообщение об ошибке
        bot.send_message(
            chat_id=chat_id, text="Произошла ошибка сервера, попробуйте позже!"
        )
        return None


# Список подкаталогов
def get_subcatalog_list(bot, API_URL, catalog_id):
    response = requests.get(f"{API_URL}list/subcatalog/?catalog_id={catalog_id}")
    subcatalogs = response.json()
    return subcatalogs


# Список продуктов
def get_product_for_subcatalog(API_URL, params, product_list):
    response = requests.get(f"{API_URL}list/product/", params=params)
    products = response.json()
    for item in products:
        product_list.append(item["product"]["id"])
    return product_list


# Список заказов
def get_order(bot, API_URL, params, chat_id):
    try:
        response = requests.get(f"{API_URL}list/order", params=params)
        orders = response.json()
        return orders
    except requests.exceptions.RequestException as e:
        # Отправляем сообщение об ошибке
        bot.send_message(
            chat_id=chat_id, text="Произошла ошибка сервера, попробуйте позже!"
        )
        return None


# Информация о заказе
def get_order_info(bot, API_URL, order_number, chat_id):
    try:
        response = requests.get(f"{API_URL}list/order-info/{order_number}/")
        order = response.json()
        text = order_info(order)
        return text
    except requests.exceptions.RequestException as e:
        # Отправляем сообщение об ошибке
        bot.send_message(
            chat_id=chat_id, text="Произошла ошибка сервера, попробуйте позже!"
        )
        return None
