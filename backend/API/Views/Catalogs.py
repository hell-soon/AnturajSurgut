from rest_framework import viewsets

from DB.models import Catalog
from API.serializers.ComponentSerializers import CatalogSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    http_method_names = ["get"]
