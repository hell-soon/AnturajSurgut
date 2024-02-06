from django.contrib.auth import get_user_model
from rest_framework import serializers
from database.models import Catalog, SubCatalog, ProductImage, Size, Product, Tags



class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'name', 'image']


class SubCatalogSerializer(serializers.ModelSerializer):
    catalog = CatalogSerializer()

    class Meta:
        model = SubCatalog
        fields = ['id', 'catalog', 'name', 'image']


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['name']



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y")
    size = SizeSerializer(many=True)
    subcatalog = SubCatalogSerializer()
    image = ProductImageSerializer(many=True)
    tags = TagsSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'tags', 'description', 'cost', 'count', 'size', 'rating', 'promotion', 'promotion_cost', 'subcatalog', 'image', 'created_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        subcatalog_data = data.pop('subcatalog')
        catalog_data = subcatalog_data.pop('catalog')
        data['catalog'] = {
            'id': catalog_data['id'],
            'name': catalog_data['name'],
            'image': catalog_data['image'],
            'subcatalog': subcatalog_data
        }

        return data

