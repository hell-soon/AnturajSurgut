from rest_framework import serializers
from order.models import Additionalservices, Order, OrderItems
from DB.models import ProductInfo
from DB.utils.codes import STATUS_MAP
from .OrderComponentSerializers import ProductQuantitySerializer


class UpdateOrderSerializer(serializers.ModelSerializer):
    items = ProductQuantitySerializer(many=True, required=False)
    order_additionalservices = serializers.PrimaryKeyRelatedField(
        queryset=Additionalservices.objects.all(), many=True, required=False
    )
    order_status = serializers.CharField(required=False)

    class Meta:
        model = Order
        fields = [
            "items",
            "order_additionalservices",
            "order_status",
        ]
        read_only_fields = ["created_at", "order_number"]

    def validate_order_additionalservices(self, value):
        existing_services = (
            self.instance.order_additionalservices.all() if self.instance else []
        )
        for service in value:
            if service in existing_services:
                raise serializers.ValidationError(
                    {
                        "order_additionalservices": f"Услуга {service} уже добавлена в заказ"
                    }
                )
        return value

    def validate_order_status(self, value):
        if (self.instance.order_status.name).lower() == "отменен":
            raise serializers.ValidationError(
                {"order_status": "Нельзя отменить уже отмененный заказ"}
            )

        if self.instance and self.instance.order_status != "1":
            raise serializers.ValidationError(
                {
                    "order_status": f"Ошибка при отмене заказа, статус: {self.instance.order_status.name}"
                }
            )

        return value

    def validate_items(self, value):
        existing_items = self.instance.orderitems_set.all() if self.instance else []

        for item in value:
            product_info_id = item["product_info_id"]
            quantity = item["quantity"]
            try:
                info = ProductInfo.objects.get(id=product_info_id)
                product_quantity = info.quantity
                total_quantity = quantity
                for existing_item in existing_items:
                    if existing_item.product.id == product_info_id:
                        total_quantity += existing_item.quantity
                if total_quantity > product_quantity:
                    raise serializers.ValidationError(
                        "Количество товара в заказе превышает количество на складе"
                    )
            except ProductInfo.DoesNotExist:
                raise serializers.ValidationError(
                    {
                        "message": "Такого товара больше не существует",
                        "product_info_id": product_info_id,
                    }
                )
        return value

    def update_items(self, instance, items_data):
        existing_items = instance.orderitems_set.all()
        for item_data in items_data:
            product_info_id = item_data["product_info_id"]
            quantity = item_data["quantity"]
            product = ProductInfo.objects.get(id=product_info_id)
            existing_item = existing_items.filter(product=product).first()
            if existing_item:
                if quantity == 0:
                    existing_item.delete()
                else:
                    existing_item.quantity = quantity
                    existing_item.save()
            elif quantity > 0:
                OrderItems.objects.create(
                    order=instance, product=product, quantity=quantity
                )

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items", None)
        if items_data is not None:
            self.update_items(instance, items_data)

        order_additionalservices = validated_data.pop("order_additionalservices", None)
        if order_additionalservices is not None:
            instance.order_additionalservices.set(order_additionalservices)

        order_status = validated_data.pop("order_status", None)
        if order_status is not None:
            instance.order_status = order_status

        instance.save()
        return instance
