from rest_framework import serializers
from DB.models import Product, ProductImage
from .ComponentSerializers import (
    SubCatalogSerializer,
    TagsSerializer,
    CompoundSerializer,
)


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
        catalog = {
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
        return catalog
