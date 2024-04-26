from rest_framework import serializers
from order.models import (
    Additionalservices,
    OrderAddress,
    LegalDate,
)
from sitedb.models import Sertificate

from .OrderUtilsSerializers import (
    OrderTypeSerializer,
    PaymentTypeSerializer,
    OrderFaceSerializer,
    OrderStatusSerializer,
)


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


class OrderUtilsSerializer(serializers.Serializer):
    order_face = OrderFaceSerializer(many=True)
    order_type = OrderTypeSerializer(many=True)
    payment_type = PaymentTypeSerializer(many=True)
    order_status = OrderStatusSerializer(many=True)


class OrderAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAddress
        fields = [
            "region",
            "city",
            "street",
            "house",
            "apartment",
            "floor",
            "post_index",
        ]


class LegalDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalDate
        fields = [
            "name",
            "inn",
            "ogrn",
            "kpp",
            "bik",
            "bank_name",
            "cores_account",
            "ras_check",
            "legal_address",
        ]
