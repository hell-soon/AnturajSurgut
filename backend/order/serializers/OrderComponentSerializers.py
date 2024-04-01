from rest_framework import serializers
from order.models import Additionalservices

from sitedb.models import Sertificate


class AdditionalservicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additionalservices
        fields = ["id", "name", "cost"]


class ProductQuantitySerializer(serializers.Serializer):
    product_info_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=0)


class SertificateSerializer(serializers.Serializer):
    class Meta:
        model = Sertificate
        fields = ["id", "code", "quantity"]
