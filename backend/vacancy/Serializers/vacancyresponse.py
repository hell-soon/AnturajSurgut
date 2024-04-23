from rest_framework import serializers
from vacancy.models import ResponseVacancy, Vacancy
from django.http import Http404
from icecream import ic


class VacancyResponseSerializer(serializers.ModelSerializer):
    vacancy_id = serializers.IntegerField()

    class Meta:
        model = ResponseVacancy
        fields = ["vacancy_id", "name", "phone"]

    def validate(self, data):
        try:
            vacancy = Vacancy.objects.get(id=data["vacancy_id"])
        except Vacancy.DoesNotExist:
            raise serializers.ValidationError({"error": ["Вакансия не найдена"]})

        if ResponseVacancy.objects.filter(
            vacancy=vacancy, phone=data["phone"]
        ).exists():
            raise serializers.ValidationError(
                {
                    "error": [
                        "Вы уже откликнулись на эту вакансию с этим номером телефона"
                    ]
                }
            )

        if vacancy.is_active is False:
            raise serializers.ValidationError({"error": ["Вакансия не активна"]})

        return data

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Номер телефона должен содержать только цифры"
            )

        if len(value) < 11:
            raise serializers.ValidationError("Номер телефона должен содержать 11 цифр")
        return value

    def create(self, validated_data):
        vacancy = Vacancy.objects.get(id=validated_data["vacancy_id"])
        user = validated_data.get(
            "user"
        )  # Получаем пользователя из валидированных данных

        # Проверяем, есть ли уже заявка от этого пользователя на эту вакансию
        if ResponseVacancy.objects.filter(vacancy=vacancy, user=user).exists():
            raise serializers.ValidationError(
                {"error": ["Вы уже откликнулись на эту вакансию"]}
            )

        validated_data["vacancy"] = vacancy
        response = ResponseVacancy.objects.create(**validated_data)
        return response
