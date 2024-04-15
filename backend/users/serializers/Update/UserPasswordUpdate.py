from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserUpdatePasswordSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ["password1", "password2"]
        extra_kwargs = {
            "password1": {"write_only": True},
            "password2": {"write_only": True},
        }

    def validate(self, data):
        """
        Проверка совпадения двух паролей и их длины
        """
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Пароли не совпадают")

        if len(data["password1"]) < 8:
            raise serializers.ValidationError(
                "Пароль должен содержать не менее 8 символов"
            )

        if data["password1"].isdigit():
            raise serializers.ValidationError(
                "Пароль не должен состоять только из цифр"
            )

        return data

    def update(self, instance, validated_data):
        """
        Обновление пароля пользователя
        """
        instance.set_password(validated_data["password1"])
        instance.save()
        return instance
