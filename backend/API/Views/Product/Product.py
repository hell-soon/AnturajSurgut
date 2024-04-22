from rest_framework import viewsets
from rest_framework.throttling import AnonRateThrottle

from django_filters import rest_framework as filters


from API.serializers.MainProductSerializers import ProductSerializer
from API.filters.ProductFilter import ProductFilter
from API.Utils.Paginator.PaginationClass import StandardResultsSetPagination

from DB.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(product_status=True).order_by("?")
    serializer_class = ProductSerializer
    http_method_names = ["get"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilter
    pagination_class = StandardResultsSetPagination
