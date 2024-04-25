from rest_framework import serializers
from order.models import (
    Additionalservices,
    OrderType,
    OrderFace,
    PaymentType,
    OrderAddress,
    LegalDate,
    OrderItems,
)
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


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ["product", "color", "size", "cost", "quantity", "total_cost"]
