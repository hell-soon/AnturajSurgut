from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework import serializers

from order.models import Order, OrderStatus, OrderItems
from reviews.models import Review
from django.core.validators import MinValueValidator, MaxValueValidator

# from order.serializers.OrderComponentSerializers import OrderItemsSerializer


class BaseorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ProfilListeOrderSerializer(BaseorderSerializer):
    order_status = serializers.CharField(source="order_status.name")
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    total_cost = serializers.FloatField(required=False)

    class Meta(BaseorderSerializer.Meta):
        fields = [
            "id",
            "order_number",
            "order_status",
            "created_at",
            "order_paymant",
            "total_cost",
        ]


class OrderItemsSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source="product.product.id")
    product_info_id = serializers.IntegerField(source="product.id")

    class Meta:
        model = OrderItems
        fields = [
            "product_id",
            "product_info_id",
            "color",
            "size",
            "cost",
            "quantity",
            "total_cost",
        ]


class ProfileDetailOrderSerializer(BaseorderSerializer):
    order_status = serializers.CharField(source="order_status.name")
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    items = serializers.SerializerMethodField()

    class Meta(BaseorderSerializer.Meta):
        fields = [
            "id",
            "order_number",
            "order_status",
            "created_at",
            "order_paymant",
            "items",
        ]

    def get_items(self, obj):
        items = obj.orderitems_set.all()
        return OrderItemsSerializer(items, many=True).data


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class UserSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "first_name", "last_name", "email", "phone", "tg_id"]


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    password_repeat = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "tg_id",
            "password",
            "password_repeat",
        ]
        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
            "phone": {"required": False},
            "email": {"required": False},
            "tg_id": {"required": False},
        }

    def validate_email(self, value):
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Пользователь с таким email уже существует"
            )
        return value

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Телефон может содержать только цифры")
        if len(value) < 11:
            raise serializers.ValidationError("Телефон должен содержать 11 цифр")
        return value

    def validate_password(self, value):
        if value:
            if len(value) < 8:
                raise serializers.ValidationError(
                    "Пароль должен быть не менее 8 символов"
                )
            if value.isdigit() or value.isalpha() or " " in value:
                raise serializers.ValidationError(
                    "Пароль должен содержать буквы, цифры и не должен содержать пробелов"
                )
        return value

    def validate(self, data):
        if data.get("password") != data.get("password_repeat"):
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)


class ProfileReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format="%d.%m.%Y")
    rating = serializers.IntegerField(
        required=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )

    class Meta:
        model = Review
        fields = ["id", "text", "rating", "created_at"]
        read_only_fields = ["created_at"]
