from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from reviews.models import Review


class ReviewChangeSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(
        required=False, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    class Meta:
        model = Review
        fields = ["id", "text", "rating"]
        read_only_fields = ["created_at"]


