from django.shortcuts import render
from rest_framework import viewsets
from .serializers.MainProductSerializers import ProductSerializer
from .serializers.DetailProductSerializers import DetailProductSerializer
from DB.models import Product, ProductInfo
from API.filters.filter import ProductFilter
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from icecream import ic
from rest_framework.generics import RetrieveAPIView
from rest_framework.exceptions import NotFound
from drf_yasg.utils import swagger_auto_schema


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["get"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilter


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
