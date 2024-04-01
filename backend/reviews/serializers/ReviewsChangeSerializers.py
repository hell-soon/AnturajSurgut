from rest_framework import serializers
from reviews.models import Review


class ReviewChangeSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, required=False)

    class Meta:
        model = Review
        fields = ["id", "text", "rating"]
        read_only_fields = ["created_at"]
