from rest_framework import serializers

from order.models import OrderFace, OrderStatus, OrderType, PaymentType


class BaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = None  # Это должно быть указано в каждом дочернем классе
        fields = ["id", "name"]


class OrderFaceSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta):
        model = OrderFace


class OrderTypeSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta):
        model = OrderType


class PaymentTypeSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta):
        model = PaymentType


class OrderStatusSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta):
        model = OrderStatus
