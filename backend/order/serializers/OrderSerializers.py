from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from order.models import (
    Additionalservices,
    Order,
    OrderItems,
    PaymentType,
    OrderType,
    OrderFace,
    OrderAddress,
    LegalDate,
)
from .OrderComponentSerializers import (
    ProductQuantitySerializer,
    OrderAddressSerializer,
    LegalDateSerializer,
)
from DB.models import ProductInfo
from sitedb.models import Sertificate


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
    payment_type = serializers.PrimaryKeyRelatedField(
        queryset=PaymentType.objects.all(), required=True
    )
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    sertificate = serializers.CharField(required=False, allow_blank=True)
    order_type = serializers.PrimaryKeyRelatedField(
        queryset=OrderType.objects.all(), required=True
    )
    order_face = serializers.PrimaryKeyRelatedField(
        queryset=OrderFace.objects.all(), required=True
    )
    address = OrderAddressSerializer(write_only=True, required=False)
    legal = LegalDateSerializer(required=False)

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
            "address",
            "order_face",
            "order_additionalservices",
            "comment",
            "order_status",
            "track_number",
            "payment_type",
            "sertificate",
            "legal",
        ]
        read_only_fields = ["created_at", "order_number"]

    def validate(self, data):
        type = data.get("order_type")
        if type.name == "Самовывоз" and data.get("address"):
            raise serializers.ValidationError(
                {"error": ["Нельзя указать адрес самовывоза"]}
            )

        if type.name != "Самовывоз" and not data.get("address"):
            raise serializers.ValidationError({"error": ["Необходимо указать адрес"]})

        order_face = data.get("order_face")
        legal_data = data.get("legal")
        if order_face and order_face.name == "Юридическое лицо" and not legal_data:
            raise serializers.ValidationError(
                {
                    "error": [
                        'Для заказа "Юридическое лицо" необходимо предоставить данные о юридическом лице.'
                    ]
                }
            )
        if not any(data.get(field) for field in ["user_email", "user_phone"]):
            raise serializers.ValidationError(
                {"error": ["Необходимо заполнить хотя бы одно из полей"]}
            )
        return data

    def validate_sertificate(self, value):
        if value:
            try:
                sertificate = Sertificate.objects.get(code=value)
            except Sertificate.DoesNotExist:
                raise ValidationError("Сертификат с таким кодом не найден.")

            current_date = timezone.now()
            if (
                not sertificate.status
                or sertificate.quanity <= 0
                or sertificate.end_date <= current_date
            ):
                if not sertificate.status:
                    raise ValidationError("Сертификат неактивен.")
                elif sertificate.quanity <= 0:
                    raise ValidationError("Сертификат закончился")
                else:
                    raise ValidationError("Срок действия сертификата истек.")

            return sertificate

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

            try:
                info = ProductInfo.objects.get(id=product_info_id)
                if quantity > info.quantity:
                    errors[index] = (
                        f"Количество товара в заказе превышает его количество на складе ({info.quantity} шт. на складе)."
                    )
            except ProductInfo.DoesNotExist:
                errors[index] = "Такого товара больше не существует"
                continue

        if errors:
            raise serializers.ValidationError(errors)

        return value

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        additional_services_data = validated_data.pop("order_additionalservices")
        address_data = validated_data.pop("address", None)
        legal_data = validated_data.pop("legal", None)

        order = Order.objects.create(**validated_data)
        order.order_additionalservices.set(additional_services_data)
        if address_data:
            OrderAddress.objects.get_or_create(order=order, **address_data)

        if legal_data:
            LegalDate.objects.get_or_create(order=order, **legal_data)

        for item_data in items_data:
            product_info_id = item_data["product_info_id"]
            quantity = item_data["quantity"]
            product = ProductInfo.objects.get(id=product_info_id)
            OrderItems.objects.create(order=order, product=product, quantity=quantity)

        return order

        """
        ОШИБКИ В ОБЩИЙ ВИД {"error": ["string"]}
        """
