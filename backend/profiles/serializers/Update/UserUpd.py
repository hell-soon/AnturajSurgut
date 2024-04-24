from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления данных пользователя
    """

    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    phone = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False)
    password1 = serializers.CharField(write_only=True, required=False)
    password2 = serializers.CharField(write_only=True, required=False)
    tg_id = serializers.IntegerField(required=False)

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "password1",
            "password2",
            "tg_id",
        ]

    def validate(self, data):
        # Проверяем, что если один из паролей был предоставлен, то оба должны быть предоставлены
        if (data.get("password1") and not data.get("password2")) or (
            not data.get("password1") and data.get("password2")
        ):
            raise serializers.ValidationError(
                {"error": "Пароли должны быть предоставлены в паре"}
            )

        # Проверяем совпадение паролей и их требования
        if data.get("password1") and data.get("password2"):
            if data["password1"] != data["password2"]:
                raise serializers.ValidationError({"error": "Пароли не совпадают"})

            if data["password1"].isdigit() or data["password1"].isalpha():
                raise serializers.ValidationError(
                    {"error": "Пароль должен содержать буквы и цифры"}
                )

            if len(data["password1"]) < 8:
                raise serializers.ValidationError(
                    {"error": "Пароль должен быть не менее 8 символов"}
                )

        # Проверяем телефон
        if data.get("phone") and not data["phone"].isdigit():
            raise serializers.ValidationError(
                {"error": "Телефон может содержать только цифры и знак '+'"}
            )

        # Проверяем имя и фамилию TODO FIX
        # if not data.get("first_name") and not data.get("last_name"):
        #     raise serializers.ValidationError(
        #         {"error": "Имя и фамилия не могут быть пустыми одновременно"}
        #     )

        # Проверяем email на уникальность
        if (
            data.get("email")
            and get_user_model().objects.filter(email=data["email"]).exists()
        ):
            raise serializers.ValidationError(
                {"error": "Пользователь с таким email уже существует"}
            )

        return data

    def validate_tg_id(self, value):
        if value == self.instance.tg_id:
            raise serializers.ValidationError("Аккаунт уже привязан")
        return value

    def update(self, instance, validated_data):
        # Обновляем имя, фамилию, телефон и email
        # instance.first_name = validated_data.get("first_name", instance.first_name)
        # instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.tg_id = validated_data.get("tg_id", instance.tg_id)
        # Обновляем пароль, если он был предоставлен
        new_password = validated_data.get("password1")
        if new_password:
            instance.set_password(new_password)

        instance.save()
        return instance
