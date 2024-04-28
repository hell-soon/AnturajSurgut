from rest_framework import serializers

from django.core.validators import MinValueValidator, MaxValueValidator

from reviews.models import Review


class ProfileReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format="%d.%m.%Y")
    rating = serializers.IntegerField(
        required=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )

    class Meta:
        model = Review
        fields = ["id", "text", "rating", "created_at"]
        read_only_fields = ["created_at"]
