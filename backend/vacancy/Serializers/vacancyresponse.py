from rest_framework import serializers
from vacancy.models import ResponseVacancy, Vacancy
from django.http import Http404
from icecream import ic


class VacancyResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResponseVacancy
        fields = ["name", "phone"]

    def validate_name(self, value):
        if value.isalpha() is False:
            raise serializers.ValidationError("Имя должно содержать только буквы")

        return value

    def validate_phone(self, value):
        if value.isdigit() is False:
            raise serializers.ValidationError(
                "Номер телефона должен содержать только цифры"
            )
        return value
