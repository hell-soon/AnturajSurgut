import phonenumbers
from rest_framework import serializers
from django.core.validators import RegexValidator
from reviews.models import Feedback


class FeedBackSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()
    name = serializers.CharField(min_length=5)

    class Meta:
        model = Feedback
        fields = ["phone", "name", "text"]

    def validate_phone(self, value):
        try:
            phone_number = phonenumbers.parse(value, "RU")
            if (
                not phonenumbers.is_valid_number(phone_number)
                or str(phone_number.country_code) != "7"
            ):
                raise serializers.ValidationError("Телефон не валиден")
            return phonenumbers.format_number(
                phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError("Телефон не валиден")

    def validate_name(self, value):
        # if value.isspace():
        #     raise serializers.ValidationError("Имя не может быть пустым")
        if not value.isalpha():
            raise serializers.ValidationError("Имя должно содержать только буквы")
        return value

    def create(self, validated_data):
        return super().create(validated_data)
