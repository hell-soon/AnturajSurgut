def addition_info_for_product(data):
    text = ""
    if data == "Информация о товаре не найдена":
        text += "Товара нет в наличии"
    else:
        for info in data:
            size = info["size"]["name"]
            color = info["color"]["name"]
            cost = info["cost"]
            if info["promotion"]:
                cost = f"{info['promotion_cost']} (Товар по акции)"
            quantity = info["quantity"]
            text += f"Размер: {size}\nЦвет: {color}\nСтоимость: {cost}\nКоличество: {quantity}\n\n"
    return text
