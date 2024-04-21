from rest_framework import serializers
from .ComponentSerializers import ColorSerializer, SizeSerializer, CompoundSerializer


class MenuSerializer(serializers.Serializer):
    color = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    compound = serializers.SerializerMethodField()

    class Meta:
        fields = ["color", "size", "compound"]

    def get_color(self, obj):
        return ColorSerializer(obj["color"], many=True).data

    def get_size(self, obj):
        return SizeSerializer(obj["size"], many=True).data

    def get_compound(self, obj):
        return CompoundSerializer(obj["compound"], many=True).data
