from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    search_data = serializers.CharField(max_length=100)

    class Meta:
        fields = ["search_data"]
