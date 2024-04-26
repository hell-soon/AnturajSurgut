from rest_framework import serializers
from .ComponentSerializers import ColorSerializer, SizeSerializer, CompoundSerializer
from API.Utils.Prices.MinMaxPrice import calculated_range_cost


class CostRangeSerializer(serializers.Serializer):
    min = serializers.IntegerField()
    max = serializers.IntegerField()


class FilterMenuSerializer(serializers.Serializer):
    color = ColorSerializer(many=True)
    size = SizeSerializer(many=True)
    compound = CompoundSerializer(many=True)
    cost_range = CostRangeSerializer(read_only=True)

    def get_cost_range(self, obj):
        cost_range = calculated_range_cost()
        return cost_range
