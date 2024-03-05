from icecream import ic
from DB.utils.codes import STATUS_MAP


def order_info(order):
    track_number = ""
    adress = ""
    status = STATUS_MAP[order["order_status"]]
    ic(order)
    if order["order_type"] == "1":
        status = "Самовывоз"
        adress = "Адрес магазина"
    if "track_number" in order and order["order_type"] != "1":
        track_number = f"Трек номер: {order['track_number']}"
        adress = f"Адрес доставки: {order['order_address']}"
    text = (
        f"Информация по заказу: <b>{order['order_number']}</b>\n\n"
        f"Статус заказа: <b>{status}</b>\n"
        f"{track_number}\n"
        f"Забрать: {adress}\n\n"
        f"Заказ сформирован: {order['created_at']}"
    )
    return text
