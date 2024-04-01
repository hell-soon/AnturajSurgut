from rest_framework import serializers
from DB.models import ProductInfo
from .ComponentSerializers import *
from icecream import ic


class DetailProductSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    size = SizeSerializer()

    class Meta:
        model = ProductInfo
        fields = [
            "id",
            "color",
            "size",
            "quantity",
            "cost",
            "promotion",
            "promotion_cost",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        info = {
            "product_info_id": data["id"],
            "color": data["color"],
            "size": data["size"],
            "quantity": data["quantity"],
            "cost": data["cost"],
            "promotion": data["promotion"],
            "promotion_cost": data["promotion_cost"],
        }
        return info
