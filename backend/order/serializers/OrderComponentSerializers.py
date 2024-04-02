from rest_framework import serializers
from order.models import Additionalservices, OrderType, OrderFace, PaymentType

from sitedb.models import Sertificate


class AdditionalservicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additionalservices
        fields = ["id", "name", "cost"]


class ProductQuantitySerializer(serializers.Serializer):
    product_info_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=0)


class SertificateSerializer(serializers.Serializer):
    class Meta:
        model = Sertificate
        fields = ["id", "code", "quantity"]


class OrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = ["id", "name"]


class OrderFaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFace
        fields = ["id", "name"]


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ["id", "name"]


class CombinedDataSerializer(serializers.Serializer):
    order_type = OrderTypeSerializer(many=True)
    order_face = OrderFaceSerializer(many=True)
    payment_type = PaymentTypeSerializer(many=True)
