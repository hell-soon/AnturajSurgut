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


class SubCatalogViewSet(viewsets.ModelViewSet):
    queryset = SubCatalog.objects.all()
    serializer_class = SubCatalogSerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = TagsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
