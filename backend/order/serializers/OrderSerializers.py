from rest_framework import serializers
from order.models import Additionalservices, Order, OrderItems
from DB.models import ProductInfo
from .OrderComponentSerializers import ProductQuantitySerializer
from rest_framework.exceptions import ValidationError
from sitedb.models import Sertificate

from django.utils import timezone
from icecream import ic


class OrderSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(required=False, allow_blank=True)
    user_phone = serializers.CharField(required=False, allow_blank=True)
    items = ProductQuantitySerializer(many=True, write_only=True)
    order_additionalservices = serializers.PrimaryKeyRelatedField(
        queryset=Additionalservices.objects.all(),
        many=True,
        write_only=True,
        required=False,
    )
    payment_type = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    sertificate = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Order
        fields = [
            "user_initials",
            "user_email",
            "user_phone",
            "items",
            "created_at",
            "order_number",
            "order_type",
            "order_address",
            "order_face",
            "order_additionalservices",
            "comment",
            "order_status",
            "track_number",
            "payment_type",
            "sertificate",
        ]
        read_only_fields = ["created_at", "order_number"]

    def validate(self, data):
        if not data.get("user_email") and not data.get("user_phone"):
            raise serializers.ValidationError(
                "Необходимо заполнить хотя бы одно из полей user_email или user_phone"
            )
        return data

    def validate_sertificate(self, value):
        if value:
            try:
                sertificate = Sertificate.objects.get(code=value)
                if (
                    not sertificate.status
                    or sertificate.quanity <= 0
                    or sertificate.end_date <= timezone.now()
                ):
                    raise ValidationError("Сертификат неактивен или закончился")
                sertificate.quanity -= 1
                sertificate.save()
                return sertificate
            except Sertificate.DoesNotExist:
                raise ValidationError("Сертификат не найден")

    def validate_items(self, value):
        for item in value:
            product_info_id = item["product_info_id"]
            quantity = item["quantity"]
            try:
                info = ProductInfo.objects.get(id=product_info_id)
                product_quantity = info.quantity
                if quantity > product_quantity:
                    raise serializers.ValidationError(
                        "Количество товара в заказе, превышает его количетсво на складе"
                    )
            except ProductInfo.DoesNotExist:
                raise serializers.ValidationError("Такого товара больше не существует")
        return value

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        additional_services_data = validated_data.pop("order_additionalservices")

        order = Order.objects.create(**validated_data)
        order.order_additionalservices.set(additional_services_data)

        for item_data in items_data:
            product_info_id = item_data["product_info_id"]
            quantity = item_data["quantity"]
            product = ProductInfo.objects.get(id=product_info_id)
            OrderItems.objects.create(order=order, product=product, quantity=quantity)

        return order
