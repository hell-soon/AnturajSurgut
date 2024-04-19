from django.contrib.auth import get_user_model
from django.utils.text import slugify
from rest_framework import serializers
from django.db import IntegrityError


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["email", "first_name", "last_name", "password1", "password2"]

    def validate(self, data):
        """
        Проверка соответствия паролей и выполнение требований к их длине и наличию цифр.
        """
        if not data.get("first_name") or not data.get("last_name"):
            raise serializers.ValidationError(
                {"error": "Имя и фамилия обязательны для заполнения."}
            )
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError({"error": "Пароли не совпадают."})

        if len(data["password1"]) < 8:
            raise serializers.ValidationError(
                {"error": "Пароль должен быть не менее 8 символов."}
            )

        if data["password1"].isdigit():
            raise serializers.ValidationError(
                {"error": "Пароль не должен состоять только из цифр."}
            )

        return data

    def validate_email(self, value):
        """
        Проверка уникальности email.
        """
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Пользователь с таким email уже существует."
            )
        return value

    def create(self, validated_data):
        """
        Создание нового пользователя на основе проверенных данных.
        """
        email = validated_data.pop("email")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        password = validated_data.pop("password1")

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
                    "error": "Пользователь с таким email уже существует. Пожалуйста, используйте другой email."
                }
            )

        return user
