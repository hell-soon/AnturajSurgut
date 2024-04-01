from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination

from DB.models import Product
from API.serializers.MainProductSerializers import ProductSerializer
from API.filters.filter import ProductFilter


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 30  # TODO change to 20
    page_size_query_param = "page_size"
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(product_status=True).order_by(
        "name", "-created_at"
    )
    serializer_class = ProductSerializer
    http_method_names = ["get"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilter
    pagination_class = StandardResultsSetPagination
