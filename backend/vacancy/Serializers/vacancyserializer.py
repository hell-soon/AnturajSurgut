from rest_framework import serializers
from vacancy.models import Vacancy


class BaseVacancySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)

    class Meta:
        model = Vacancy
        fields = "__all__"


class VacancySerializer(BaseVacancySerializer):
    class Meta(BaseVacancySerializer.Meta):
        model = Vacancy
        fields = ("id", "name", "salary")
