from database.models import Additionalservices, Order, OrderItems, Product
from rest_framework import serializers


class AdditionalservicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additionalservices
        fields = ["id"]


class ProductQuantitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


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
        # Validate that each product exists and has a valid quantity
        for item in value:
            product_id = item["id"]
            try:
                Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                raise serializers.ValidationError("Такого товара больше не существует")
        return value

    def create(self, validated_data):
        # Extract the items data from the validated data
        items_data = validated_data.pop("items")
        # Extract the additional services data from the validated data
        additional_services_data = validated_data.pop("order_additionalservices")
        # Create the order instance
        order = Order.objects.create(**validated_data)
        # Add the additional services to the order
        order.order_additionalservices.set(additional_services_data)
        # Create the order items
        for item_data in items_data:
            product_id = item_data["id"]
            quantity = item_data["quantity"]
            product = Product.objects.get(id=product_id)
            OrderItems.objects.create(order=order, product=product, quantity=quantity)

        return order
