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
from DB.models import Product, ProductInfo
from icecream import ic


class AdditionalservicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additionalservices
        fields = ["id", "name", "cost"]


class ProductQuantitySerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=True)
    color_id = serializers.IntegerField(required=True)
    size_id = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(min_value=1, required=True)

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value, product_status=True).exists():
            raise serializers.ValidationError("Товар не активен")
        return value

    def validate(self, data):
        product_id = data.get("product_id")
        product_info = ProductInfo.objects.filter(
            product_id=product_id,
            color_id=data.get("color_id"),
            size_id=data.get("size_id"),
        ).first()

        if not product_info:
            raise serializers.ValidationError({"error": "Товара нет в наличии"})

        if data["quantity"] > product_info.quantity:
            raise serializers.ValidationError(
                {"error": "Количество больше чем есть на складе"}
            )

        return data


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
