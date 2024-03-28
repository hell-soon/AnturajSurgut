from rest_framework import serializers
from order.models import Additionalservices, Order, OrderItems
from DB.models import ProductInfo
from .OrderComponentSerializers import ProductQuantitySerializer
from rest_framework.exceptions import ValidationError
from sitedb.models import Sertificate
from django.db.models import Q
from django.utils import timezone
from icecream import ic
from django.shortcuts import get_object_or_404


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
        if not any(data.get(field) for field in ["user_email", "user_phone"]):
            raise serializers.ValidationError(
                {"user_error": "Необходимо заполнить хотя бы одно из полей"}
            )
        return data

    def validate_sertificate(self, value):
        if value:
            try:
                sertificate = Sertificate.objects.get(code=value)
            except Sertificate.DoesNotExist:
                raise ValidationError(
                    {"sertificate": "Сертификат с таким кодом не найден."}
                )

            current_date = timezone.now()
            if (
                not sertificate.status
                or sertificate.quanity <= 0
                or sertificate.end_date <= current_date
            ):
                if not sertificate.status:
                    raise ValidationError("Сертификат неактивен.")
                elif sertificate.quanity <= 0:
                    raise ValidationError({"sertificate": "Сертификат закончился"})
                else:
                    raise ValidationError("Срок действия сертификата истек.")

            return sertificate

    # V1
    # def validate_items(self, value):
    #     for item in value:
    #         product_info_id = item["product_info_id"]
    #         quantity = item["quantity"]
    #         try:
    #             info = ProductInfo.objects.get(id=product_info_id)
    #             if quantity > info.quantity:
    #                 raise serializers.ValidationError(
    #                     "Количество товара в заказе, превышает его количетсво на складе"
    #                 )
    #         except ProductInfo.DoesNotExist:
    #             raise serializers.ValidationError("Такого товара больше не существует")
    #     return value
    
    def validate_items(self, value):
        errors = {}
        for index, item in enumerate(value):
            product_info_id = item.get("product_info_id")
            quantity = item.get("quantity")
            if not product_info_id or not quantity:
                errors[index] = (
                    "Необходимо указать product_info_id и quantity для каждого товара."
                )
                continue

            info = get_object_or_404(ProductInfo, id=product_info_id)
            if quantity > info.quantity:
                errors[index] = (
                    f"Количество товара в заказе превышает его количество на складе ({info.quantity} шт. на складе)."
                )

        if errors:
            raise serializers.ValidationError(errors)

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
