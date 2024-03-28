from rest_framework import viewsets
from django_filters import rest_framework as filters

from DB.models import Product
from API.serializers.MainProductSerializers import ProductSerializer
from API.filters.filter import ProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["get"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilter
