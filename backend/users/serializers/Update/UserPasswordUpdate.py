from django.contrib.auth import get_user_model
from rest_framework import serializers


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
