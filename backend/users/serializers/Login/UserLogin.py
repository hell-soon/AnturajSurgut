from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate


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
