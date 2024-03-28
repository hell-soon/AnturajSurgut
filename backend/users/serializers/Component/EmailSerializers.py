from rest_framework import serializers


class UserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
