from rest_framework import serializers
from sitedb.models import Slider


class SliderSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Slider
        fields = ["id", "text", "image", "created_at"]
