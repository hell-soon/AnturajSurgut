from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserUpdatePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_repeat = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ["password", "password_repeat"]
        extra_kwargs = {
            "password": {"write_only": True},
            "password_repeat": {"write_only": True},
        }

    def validate(self, data):
        if data["password"].isdigit():
            raise serializers.ValidationError(
                {"error": ["Пароль не должен состоять только из цифр"]}
            )
        if len(data["password"]) < 8:
            raise serializers.ValidationError(
                {"error": ["Пароль должен быть не менее 8 символов"]}
            )
        if data["password"] != data["password_repeat"]:
            raise serializers.ValidationError({"error": ["Пароли не совпадают"]})

        return data

    def update(self, instance, validated_data):
        """
        Обновление пароля пользователя
        """
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
