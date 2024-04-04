from order.models import OrderFace


class OrderFaceCreator:
    def create(self):
        order_face = [
            OrderFace(name="Юридическое лицо"),
            OrderFace(name="Физическое лицо"),
        ]
        OrderFace.objects.bulk_create(order_face)
        return order_face
