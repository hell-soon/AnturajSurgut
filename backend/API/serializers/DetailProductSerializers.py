from rest_framework import serializers
from DB.models import Product, Size, Color

from .ComponentSerializers import ColorSerializer, SizeSerializer, TypeSerializer
from icecream import ic


class PriceSerializer(serializers.Serializer):
    promotion = serializers.BooleanField()
    promotion_cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity = serializers.IntegerField()


class SizeV2Serializer(serializers.Serializer):
    size = serializers.CharField()
    price = PriceSerializer()


class TestSerializer(serializers.Serializer):
    size = serializers.SerializerMethodField()
    cost = serializers.IntegerField()
    promotion = serializers.BooleanField()
    promotion_cost = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def get_size(self, obj):
        size = Size.objects.get(id=obj["size"])
        return SizeSerializer(size).data


class DetailProductSerializer(serializers.ModelSerializer):
    info = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "info",
        ]

    def get_info(self, obj):
        colors_query = obj.productinfo_set.values("color").distinct()
        color_list = []

        for color_data in colors_query:
            color_id = color_data["color"]
            color = ColorSerializer(Color.objects.get(id=color_id)).data

            sizes_query = obj.productinfo_set.filter(color=color_id).values(
                "size", "promotion", "promotion_cost", "cost", "quantity"
            )

            sizes = [TestSerializer(size).data for size in sizes_query]

            color_list.append(
                {
                    "color": color,
                    "sizes": sizes,
                }
            )

        return color_list
