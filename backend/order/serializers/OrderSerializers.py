from rest_framework import serializers
from order.models import Additionalservices
from DB.models import ProductInfo, Product
from icecream import ic
from order.models import Order, OrderItems
from .OrderComponentSerializers import (
    ProductQuantitySerializer,
    AdditionalservicesSerializer,
)


class OrderSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(required=False, allow_blank=True)
    user_phone = serializers.CharField(required=False, allow_blank=True)
    items = ProductQuantitySerializer(many=True, write_only=True)
    order_additionalservices = serializers.PrimaryKeyRelatedField(
        queryset=Additionalservices.objects.all(), many=True, write_only=True
    )

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
        ]
        read_only_fields = ["created_at", "order_number"]

    def validate(self, data):
        if not data.get("user_email") and not data.get("user_phone"):
            raise serializers.ValidationError(
                "Необходимо заполнить хотя бы одно из полей user_email или user_phone"
            )
        return data

    def validate_items(self, value):
        for item in value:
            product_info_id = item["id"]
            quantity = item["quantity"]
            try:
                info = ProductInfo.objects.get(id=product_info_id)
                product_quantity = info.quantity
                if quantity > product_quantity:
                    raise serializers.ValidationError(
                        f"Количество товара '{info.product.name}' в заказе превышает количество на складе"
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
            product_info_id = item_data["id"]
            quantity = item_data["quantity"]
            product = ProductInfo.objects.get(id=product_info_id)
            OrderItems.objects.create(order=order, product=product, quantity=quantity)

        return order


class UpdateOrderSerializer(serializers.ModelSerializer):
    items = ProductQuantitySerializer(many=True, required=False)
    order_additionalservices = serializers.PrimaryKeyRelatedField(
        queryset=Additionalservices.objects.all(), many=True, required=False
    )

    class Meta:
        model = Order
        fields = [
            "items",
            "order_additionalservices",
        ]
        read_only_fields = ["created_at", "order_number"]

    def validate_items(self, value):
        # Validate that each product exists and has a valid quantity
        for item in value:
            product_id = item["id"]
            try:
                Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                raise serializers.ValidationError("Такого товара больше не существует")
        return value

    def update(self, instance, validated_data):
        # Update the order items
        if "items" in validated_data:
            instance.orderitems_set.all().delete()  # Delete existing order items
            items_data = validated_data.pop("items")
            for item_data in items_data:
                product_id = item_data["id"]
                quantity = item_data["quantity"]
                product = Product.objects.get(id=product_id)
                OrderItems.objects.create(
                    order=instance, product=product, quantity=quantity
                )

        # Update the additional services of the order
        if "order_additionalservices" in validated_data:
            instance.order_additionalservices.set(
                validated_data["order_additionalservices"]
            )

        instance.save()
        return instance
