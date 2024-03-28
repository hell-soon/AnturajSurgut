from sitedb.models import Slider
from rest_framework import serializers


class SliderSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Slider
        fields = ["id", "is_active", "text", "image", "created_at"]
