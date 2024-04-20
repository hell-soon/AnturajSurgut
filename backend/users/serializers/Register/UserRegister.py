from django.contrib.auth import get_user_model
from django.utils.text import slugify
from rest_framework import serializers
from django.db import IntegrityError


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    password_repeat = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ["email", "first_name", "last_name", "password", "password_repeat"]

    def validate_email(self, value):
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Пользователь с таким email уже существует."
            )
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Пароль должен быть не менее 8 символов.")

        if value.isdigit():
            raise serializers.ValidationError(
                "Пароль не должен состоять только из цифр."
            )

    def validate(self, data):
        if data["password"] != data["password_repeat"]:
            raise serializers.ValidationError({"error": ["Пароли не совпадают."]})

        return data

    def create(self, validated_data):
        """
        Создание нового пользователя на основе проверенных данных.
        """
        email = validated_data.pop("email")
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")
        password = validated_data.pop("password")

        base_username = slugify(f"{first_name}-{last_name}")
        username = base_username
        suffix = 1

        while get_user_model().objects.filter(username=username).exists():
            username = f"{base_username}-{suffix}"
            suffix += 1

        try:
            user = get_user_model().objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
        except IntegrityError as e:
            raise serializers.ValidationError(
                {
                    "error": [
                        "Пользователь с таким email уже существует. Пожалуйста, используйте другой email."
                    ]
                }
            )

        return user
