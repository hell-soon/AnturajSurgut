def quantity_check(old_quantity, new_quantity, product):
    """
    Обновляет количество товара в зависимости от изменения количества в заказе
    """
    if new_quantity < old_quantity:
        product.quantity += old_quantity - new_quantity
    elif new_quantity > old_quantity:
        product.quantity -= new_quantity - old_quantity
    else:
        # Если количество не изменилось, ничего не делаем
        return product

    # Сохраняем изменения в базе данных
    product.save()
    return product
