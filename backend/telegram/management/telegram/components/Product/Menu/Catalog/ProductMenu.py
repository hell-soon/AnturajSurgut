from .....Utils.APIResponses import get_main_product
from .....Func.ProductView import show_product


def product_list_start(message, bot, API_URL, subcatalog_id):
    if message.chat.type == "private":
        product_type = "catalog"
        product_ids = get_main_product(
            API_URL, product_type, subcatalog_id=subcatalog_id
        )
        index = 0
        ids = show_product(bot, message, product_ids, index, API_URL)
        return ids
