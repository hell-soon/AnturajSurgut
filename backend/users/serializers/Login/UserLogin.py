from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        user = authenticate(email=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError(
                {"error": ["Почта или пароль были указаны неверно"]}
            )

        return user
