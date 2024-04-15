from rest_framework import serializers
from sitedb.models import Slider


class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = ["id", "text", "image", "url"]
