from django_filters import rest_framework as filters
from rest_framework import viewsets

from .filters.filter import ProductFilter
from .serializers import (
    CatalogSerializer,
    SubCatalogSerializer,
    ProductImageSerializer,
    SizeSerializer,
    ProductSerializer,
    TagsSerializer,
)
from database.models import Catalog, SubCatalog, ProductImage, Size, Product


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    http_method_names = ["get"]


class SubCatalogViewSet(viewsets.ModelViewSet):
    queryset = SubCatalog.objects.all()
    serializer_class = SubCatalogSerializer
    http_method_names = ["get"]


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    http_method_names = ["get"]


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    http_method_names = ["get"]


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = TagsSerializer
    http_method_names = ["get"]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
    http_method_names = ["get"]
