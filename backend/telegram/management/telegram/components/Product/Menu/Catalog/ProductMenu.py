from telegram.management.telegram.Utils.APIResponses import (
    get_product,
)
from telegram.management.telegram.components.Product.Menu.Popular.PopularComponent import (
    show_product,
)


def product_list(message, bot, API_URL, subcatalog_id):
    products = get_product(bot, API_URL, subcatalog_id, high_rating=False)
    index = 0
    show_product(bot, message, products, index, API_URL)
