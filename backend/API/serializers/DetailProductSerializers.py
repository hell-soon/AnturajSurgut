from rest_framework import serializers
from DB.models import ProductInfo
from .ComponentSerializers import ColorSerializer, SizeSerializer


class DetailProductSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    size = SizeSerializer()
    product_info_id = serializers.IntegerField(source="id")

    class Meta:
        model = ProductInfo
        fields = [
            "product_info_id",
            "color",
            "size",
            "quantity",
            "cost",
            "promotion",
            "promotion_cost",
        ]
