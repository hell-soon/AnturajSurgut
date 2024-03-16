from rest_framework import viewsets
from django_filters import rest_framework as filters

from DB.models import SubCatalog
from API.serializers.ComponentSerializers import SubCatalogSerializer
from API.filters.SubCatalogFilter import SubCatalogFilter


class SubCatalogViewSet(viewsets.ModelViewSet):
    queryset = SubCatalog.objects.all()
    serializer_class = SubCatalogSerializer
    http_method_names = ["get"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = SubCatalogFilter