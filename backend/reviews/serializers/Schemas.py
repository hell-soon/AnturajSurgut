from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from drf_yasg import openapi


class SchemaRewiewCreateSerializer(serializers.Serializer):
    text = serializers.CharField()
    rating = serializers.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )


class SuccessSerializer(serializers.Serializer):
    message = serializers.CharField()


class FieldSerializer(serializers.Serializer):
    message = serializers.CharField()


class ErrorSerializer(serializers.Serializer):
    field_name = FieldSerializer(many=True)


class AuthArrayObject(serializers.Serializer):
    token_class = serializers.CharField()
    token_type = serializers.CharField()
    message = serializers.CharField()


class AuthShema(serializers.Serializer):
    details = serializers.CharField()
    code = serializers.CharField()
    message = AuthArrayObject(many=True)

    def schema():
        return openapi.Response(description="Вы не авторизованы", schema=AuthShema())
