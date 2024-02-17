from django.contrib.auth import get_user_model
from rest_framework import serializers
from database.models import Catalog, SubCatalog, ProductImage, Size, Product, Tags


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["name"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image"]


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ["name"]


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ["id", "name", "image"]


class SubCatalogSerializer(serializers.ModelSerializer):
    catalog = CatalogSerializer()

    class Meta:
        model = SubCatalog
        fields = ["id", "catalog", "name", "image"]


class ProductSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y")
    size = SizeSerializer(many=True)
    subcatalog = SubCatalogSerializer()
    image = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "created_at",
            "name",
            "description",
            "count",
            "size",
            "cost",
            "rating",
            "promotion",
            "promotion_cost",
            "subcatalog",
            "image",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        subcatalog_data = data.pop("subcatalog")
        catalog_data = subcatalog_data.pop("catalog")
        catalog = {
            "catalog_id": catalog_data["id"],
            "catalog_name": catalog_data["name"],
            "catalog_image": catalog_data["image"],
            "subcatalog": {
                "subcatalog_id": subcatalog_data["id"],
                "subcatalog_name": subcatalog_data["name"],
                "subcatalog_image": subcatalog_data["image"],
                "products": [data],
            },
        }
        return catalog
