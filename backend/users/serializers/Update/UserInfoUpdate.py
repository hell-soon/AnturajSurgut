from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления данных пользователя
    # TODO: Добавить дополнительные проверки, безопаснотсь и т.д.
    """

    first_name = serializers.CharField(write_only=True, required=False)
    last_name = serializers.CharField(write_only=True, required=False)
    phone = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "phone", "email", "password"]
        extra_fields = {"email": {"read_only": True}}

        def update(self, instance, validated_data):
            instance.first_name = validated_data.get("first_name", instance.first_name)
            instance.last_name = validated_data.get("last_name", instance.last_name)
            instance.phone = validated_data.get("phone", instance.phone)
            instance.password = validated_data.get("password", instance.password)
            instance.save()
            return instance
