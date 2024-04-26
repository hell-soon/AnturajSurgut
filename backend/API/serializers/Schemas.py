from rest_framework import serializers
from .ProductSerializers import ProductSerializer
from .DetailProductSerializers import DetailProductSerializer


class ProductInfoResponse(serializers.Serializer):
    product = ProductSerializer(read_only=True)
    product_info = DetailProductSerializer(read_only=True, many=True)
