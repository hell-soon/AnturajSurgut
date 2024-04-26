from rest_framework import serializers
from DB.models import Product, ProductImage, ProductInfo
from .ComponentSerializers import (
    SubCatalogSerializer,
    TagsSerializer,
    CompoundSerializer,
)
from .DetailProductSerializers import DetailProductSerializer
from .ComponentSerializers import *


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image",)


class ProductSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True)
    image = ProductImageSerializer(many=True)
    compound = CompoundSerializer(many=True)
    sub_catalog = SubCatalogSerializer()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "image",
            "sub_catalog",
            "tags",
            "compound",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        product_catalog = data["sub_catalog"].pop("catalog")
        product_subcatalog = data.pop("sub_catalog")

        new_data = {
            "catalog": {
                "id": product_catalog["id"],
                "name": product_catalog["name"],
                "image": product_catalog["image"],
                "subcatalog": {
                    "id": product_subcatalog["id"],
                    "name": product_subcatalog["name"],
                    "image": product_subcatalog["image"],
                },
            },
            "product": data,
        }
        return new_data


class Test(serializers.ModelSerializer):
    color = ColorSerializer()
    size = SizeSerializer()
    product_info_id = serializers.IntegerField(source="id")

    class Meta:
        model = ProductInfo
        fields = [
            "product",
            "product_info_id",
            "color",
            "size",
            "quantity",
            "cost",
            "promotion",
            "promotion_cost",
        ]


class TestV2(serializers.Serializer):
    product = ProductSerializer(read_only=True)
    product_info = DetailProductSerializer(read_only=True, many=True)
