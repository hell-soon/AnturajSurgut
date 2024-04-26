from rest_framework import viewsets
from django_filters import rest_framework as filters

from API.Filters.TagsFilter import TagsFilter
from API.serializers.ComponentSerializers import TagsSerializer
from backend.paginator import StandardResultsSetPagination

from DB.models import Tags


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all().order_by("id")
    serializer_class = TagsSerializer
    http_method_names = ["get"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TagsFilter
    pagination_class = StandardResultsSetPagination
