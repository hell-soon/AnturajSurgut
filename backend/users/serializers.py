from django.utils.text import slugify
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.db import IntegrityError
from database.models import Order, Additionalservices, Product, OrderItems
from rest_framework.exceptions import ValidationError
from ProductAPI.serializers import ProductSerializer


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = get_user_model()
        fields = ["email", "password", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        """
        Проверка пароля на длинну
        Можно добавить дополнительные проверки
        :param str: value(password)
        :return: str: value(password)
        """

        if len(value) < 8:
            raise serializers.ValidationError(
                "Пароль должен содержать не менее 8 символов"
            )

        if value.isdigit():
            raise serializers.ValidationError(
                "Пароль не должен состоять только из цифр"
            )
        return value

    def validate_email(self, value):
        """Проверка уникальности

        Args:
            value (str): valeu

        Raises:
            serializers.ValidationError: Аккаунт с такой почтой уже существует

        Returns:
            str: value(email)
        """
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError("Аккаунт с такой почтой уже существует")
        return value

    def validate(self, data):
        """

        Args:
            data (_type_): _description_

        Raises:
            serializers.ValidationError: Проверка полей имя и фамилия для генероации username

        Returns:
            dict: data
        """
        if not data.get("first_name") or not data.get("last_name"):
            raise serializers.ValidationError("Необходимо указать имя и фамилию")
        return data

    def create(self, validated_data):
        """
        Args:
            validated_data : dict

        Raises:
            serializers.ValidationError: Дополнительная проверка уникальности

        Returns:
            objects: user
        """
        email = validated_data.pop("email")  # Удаляем email из валидированных данных
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")

        base_username = slugify(f"{first_name}-{last_name}")
        username = base_username
        suffix = 1

        while get_user_model().objects.filter(username=username).exists():
            username = f"{base_username}-{suffix}"
            suffix += 1

        try:
            # Передаем email при создании пользователя
            user = get_user_model().objects.create_user(
                username=username, email=email, **validated_data
            )
        except IntegrityError as e:
            raise serializers.ValidationError(
                "Данный email уже зарегистрирован. Пожалуйста, используйте другой email."
            )

        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        """
        Валидность данных для аутентификации
        Можно добавить дополнительные проверки
        :param data: data
        :return: data
        """
        email = data.get("email")
        password = data.get("password")
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError(
                    "Email или пароль были указаны неверно"
                )
        else:
            raise serializers.ValidationError(
                "Для входа в учетную запись нужно указать Email и пароль"
            )

        data["user"] = user
        return data


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления данных пользователя
    # TODO: Добавить дополнительные проверки, безопаснотсь и т.д.
    """

    first_name = serializers.CharField(write_only=True, required=False)
    last_name = serializers.CharField(write_only=True, required=False)
    phone = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "phone", "email", "password"]
        extra_fields = {"email": {"read_only": True}}

        def update(self, instance, validated_data):
            instance.first_name = validated_data.get("first_name", instance.first_name)
            instance.last_name = validated_data.get("last_name", instance.last_name)
            instance.phone = validated_data.get("phone", instance.phone)
            instance.password = validated_data.get("password", instance.password)
            instance.save()
            return instance


class UserUpdatePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = [
            "password",
        ]
        extra_fields = {"password": {"write_only": True}}

    def validate_password(self, value):
        """
        Проверка пароля на длинну
        Можно добавить дополнительные проверки
        :param str: value(password)
        :return: str: value(password)
        """
        if len(value) < 8:
            raise serializers.ValidationError(
                "Пароль должен содержать не менее 8 символов"
            )

        if value.isdigit():
            raise serializers.ValidationError(
                "Пароль не должен состоять только из цифр"
            )
        return value


class UserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class AdditionalservicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additionalservices
        fields = ["id"]


class ProductQuantitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class OrderSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(required=False, allow_blank=True)
    user_phone = serializers.CharField(required=False, allow_blank=True)
    items = ProductQuantitySerializer(many=True, write_only=True)
    order_additionalservices = serializers.PrimaryKeyRelatedField(
        queryset=Additionalservices.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Order
        fields = [
            "user_initials",
            "user_email",
            "user_phone",
            "items",
            "created_at",
            "order_number",
            "order_type",
            "order_address",
            "order_face",
            "order_additionalservices",
            "comment",
        ]
        read_only_fields = ["created_at", "order_number"]

    def validate(self, data):
        if not data.get("user_email") and not data.get("user_phone"):
            raise serializers.ValidationError(
                "Необходимо заполнить хотя бы одно из полей user_email или user_phone"
            )
        return data

    def validate_items(self, value):
        # Validate that each product exists and has a valid quantity
        for item in value:
            product_id = item["id"]
            try:
                Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                raise serializers.ValidationError("Такого товара больше не существует")
        return value

    def create(self, validated_data):
        # Extract the items data from the validated data
        items_data = validated_data.pop("items")
        # Extract the additional services data from the validated data
        additional_services_data = validated_data.pop("order_additionalservices")
        # Create the order instance
        order = Order.objects.create(**validated_data)
        # Add the additional services to the order
        order.order_additionalservices.set(additional_services_data)
        # Create the order items
        for item_data in items_data:
            product_id = item_data["id"]
            quantity = item_data["quantity"]
            product = Product.objects.get(id=product_id)
            OrderItems.objects.create(order=order, product=product, quantity=quantity)

        return order
