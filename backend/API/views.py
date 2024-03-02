from rest_framework import viewsets
from .serializers.MainProductSerializers import ProductSerializer
from .serializers.DetailProductSerializers import DetailProductSerializer
from .serializers.DetailProductSerializers import (
    CatalogSerializer,
    SubCatalogSerializer,
)
from DB.models import Product, ProductInfo, Catalog, SubCatalog
from API.filters.filter import ProductFilter
from API.filters.SubCatalogFilter import SubCatalogFilter
from API.filters.OrderFilter import OrderFilter
from django_filters import rest_framework as filters
from order.serializers.OrderSerializers import OrderSerializer
from order.models import Order
from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework.exceptions import NotFound


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["get"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilter


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    http_method_names = ["get"]


class SubCatalogViewSet(viewsets.ModelViewSet):
    queryset = SubCatalog.objects.all()
    serializer_class = SubCatalogSerializer
    http_method_names = ["get"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = SubCatalogFilter


class ProductInfoView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            if not product.product_status:
                return Response("Товар не активен")
            else:
                product_info = ProductInfo.objects.filter(product_id=product_id)
                if not product_info:
                    return Response("Информация о товаре не найдена")
                if product_info.exists():
                    serializer = DetailProductSerializer(product_info, many=True)
                    return Response(serializer.data)
                else:
                    return Response("Товара нет в наличии")
        except Product.DoesNotExist:
            raise NotFound("Товар не найден")


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ["get"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = OrderFilter


class OrderInfoView(APIView):
    def get(self, request, order_number):
        order = Order.objects.get(order_number=order_number)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
