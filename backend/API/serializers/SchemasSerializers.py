from rest_framework import serializers
from .MainProductSerializers import ProductSerializer
from .DetailProductSerializers import DetailProductSerializer


class SchemaInfoProductSerializer(serializers.Serializer):
    product = ProductSerializer()
    product_info = DetailProductSerializer()

    class Meta:
        fields = ["product", "product_info"]
