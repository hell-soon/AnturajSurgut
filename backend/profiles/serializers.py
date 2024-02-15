from django.contrib.auth import get_user_model
from rest_framework import serializers
from database.models import Cart, CartItem
from ProductAPI.serializers import ProductSerializer
from database.models import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "first_name", "last_name", "email", "phone"]


class CartSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all()
    )

    class Meta:
        model = Cart
        fields = ["user", "products", "total_cost"]

    def get_user(self, obj):
        return {"id": obj.user.id}

    def get_total_cost(self, obj):
        return obj.total_cost()
