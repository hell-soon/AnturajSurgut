from order.models import OrderFace


class OrderFaceCreator:
    def create(self, order_settings):
        order_face = [
            OrderFace(settings=order_settings, name="Юридическое лицо"),
            OrderFace(settings=order_settings, name="Физическое лицо"),
        ]
        OrderFace.objects.bulk_create(order_face)
        return order_face
