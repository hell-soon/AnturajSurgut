def quantity_check(old_quantity, new_quantity, product):
    """
    Обновляет количество товара в зависимости от изменения количества в заказе
    """
    if new_quantity == old_quantity:
        pass
    elif new_quantity < old_quantity:
        product.quantity += old_quantity - new_quantity
    elif new_quantity > old_quantity:
        product.quantity -= new_quantity - old_quantity
    # Сохраняем изменения в базе данных
    product.save()
