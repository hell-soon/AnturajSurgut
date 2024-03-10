from rest_framework import serializers
from DB.models import *


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ["id", "name", "image"]


class SubCatalogSerializer(serializers.ModelSerializer):
    catalog = CatalogSerializer()

    class Meta:
        model = SubCatalog
        fields = ["id", "catalog", "name", "image"]


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ["name"]


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["id", "color"]


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["id", "name"]


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ["id", "name"]
