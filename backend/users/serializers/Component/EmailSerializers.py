from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Пользователь с таким email не существует."
            )
        return value
