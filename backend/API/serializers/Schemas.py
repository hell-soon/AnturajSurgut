from rest_framework import serializers
from .ProductSerializers import ProductSerializer
from .DetailProductSerializers import DetailProductSerializer


class ProductInfoResponse(serializers.Serializer):
    product = ProductSerializer(read_only=True)
    product_info = DetailProductSerializer(read_only=True, many=True)


class ProductPaginationSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    next = serializers.URLField(allow_null=True)
    previous = serializers.URLField(allow_null=True)
    results = ProductSerializer(many=True)
