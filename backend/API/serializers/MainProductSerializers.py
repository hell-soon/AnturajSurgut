from rest_framework import serializers
from DB.models import Product, ProductImage
from .ComponentSerializers import SubCatalogSerializer, TagsSerializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image",)


class ProductSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True)
    image = ProductImageSerializer(many=True)
    sub_catalog = SubCatalogSerializer()
    created_at = serializers.DateTimeField(format="%d.%m.%Y")

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "image",
            "sub_catalog",
            "tags",
            "product_status",
            "created_at",
        )

    def validate(self, data):
        product_id = data.get("id")
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Товар с указанным ID не найден")
        return data

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
