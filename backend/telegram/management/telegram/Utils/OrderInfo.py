from icecream import ic
from DB.utils.codes import STATUS_MAP


def order_info(order):
    track_number = ""
    adress = ""
    status = STATUS_MAP[order["order_status"]]
    if "track_number" in order and order["order_type"] != "1":
        track_number = f"Трек номер: {order['track_number']}"
        adress = f"Адрес доставки: {order['order_address']}"

    text = (
        f"Информация о заказе: {order['order_number']}\n"
        f"Статус заказа: {status}\n"
        f"{track_number}\n"
        f"{adress}\n"
        f"Заказ сформирован: {order['created_at']}\n"
    )
    return text
