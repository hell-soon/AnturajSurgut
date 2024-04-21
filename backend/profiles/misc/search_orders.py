from order.models import Order
from DB.utils.codes import STATUS_MAP
from django.db.models import Q


def get_user_order(user):
    orders = Order.objects.filter(Q(user_email=user.email) | Q(user_phone=user.phone))
    order_list = []
    if orders:
        for order in orders:
            order_dict = {}
            order_dict["order_number"] = order.order_number
            order_dict["order_status"] = STATUS_MAP[order.order_status]
            order_dict["created_at"] = order.created_at.strftime("%d.%m.%Y" + " %H:%M")
            order_list.append(order_dict)
        return order_list
    return None
