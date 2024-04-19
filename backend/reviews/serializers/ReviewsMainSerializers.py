from rest_framework import serializers
from reviews.models import Review
from .ReviewsComponentsSerializers import ReviewsUsersSerializer
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator


class ReviewSerializer(serializers.ModelSerializer):
    user = ReviewsUsersSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, format="%d.%m.%Y")
    rating = serializers.IntegerField(
        required=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )

    class Meta:
        model = Review
        fields = ["user", "text", "rating", "created_at"]
        read_only_fields = ["created_at"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_representation = ReviewsUsersSerializer(instance.user).data
        representation["user"] = user_representation
        return representation
