from rest_framework import serializers
from order.models import Order, OrderItems


class BaseorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ProfilListeOrderSerializer(BaseorderSerializer):
    order_status = serializers.CharField(source="order_status.name")
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")

    class Meta(BaseorderSerializer.Meta):
        fields = [
            "id",
            "order_number",
            "order_status",
            "created_at",
            "order_paymant",
        ]


class OrderItemsSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source="product.product.id")
    product_info_id = serializers.IntegerField(source="product.id")

    class Meta:
        model = OrderItems
        fields = [
            "product_id",
            "product_info_id",
            "color",
            "size",
            "cost",
            "quantity",
            "total_cost",
        ]


class ProfileDetailOrderSerializer(BaseorderSerializer):
    order_status = serializers.CharField(source="order_status.name")
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    items = serializers.SerializerMethodField()

    class Meta(BaseorderSerializer.Meta):
        fields = [
            "id",
            "order_number",
            "order_status",
            "created_at",
            "order_paymant",
            "items",
        ]

    def get_items(self, obj):
        items = obj.orderitems_set.all()
        return OrderItemsSerializer(items, many=True).data
