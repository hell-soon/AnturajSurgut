from django.contrib.auth import get_user_model


from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
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
