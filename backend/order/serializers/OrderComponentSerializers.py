from rest_framework import serializers
from order.models import Additionalservices
from DB.models import Product


class AdditionalservicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additionalservices
        fields = ["id"]


class ProductQuantitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)
