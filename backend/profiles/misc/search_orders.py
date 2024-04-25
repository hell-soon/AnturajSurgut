from order.models import Order
from django.db.models import Q
from icecream import ic


def get_user_order(user):
    orders = Order.objects.filter(
        Q(user_email=user.email) | Q(user_phone=user.phone)
    ).order_by("-created_at")
    order_list = []
    if orders:
        for order in orders[:20]:  # Изменение здесь
            order_dict = {}
            order_dict["id"] = order.id
            order_dict["order_number"] = order.order_number
            order_dict["order_status"] = order.order_status.name
            order_dict["created_at"] = order.created_at.strftime("%d.%m.%Y" + " %H:%M")
            order_list.append(order_dict)
        return order_list
    return None
