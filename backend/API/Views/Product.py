from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.decorators import action


from django_filters import rest_framework as filters

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from backend.paginator import StandardResultsSetPagination


from API.serializers.ProductSerializers import ProductSerializer
from API.serializers.Schemas import ProductInfoResponse
from API.Filters.ProductFilter import ProductFilter
from API.serializers.DetailProductSerializers import DetailProductSerializer

from DB.models import Product, ProductInfo


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(product_status=True).order_by("?")
    serializer_class = ProductSerializer
    http_method_names = ["get"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilter
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(
        responses={
            200: ProductInfoResponse(),
            400: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={"detail": openapi.Schema(type=openapi.TYPE_STRING)},
            ),
        }
    )
    @action(detail=True, methods=["get"])
    def info(self, request, pk=None):
        responce_data = {}  
        product = self.get_object()
        product_info = ProductInfo.objects.filter(product=product)
        product_serializer = self.get_serializer_class()(
            product, context={"request": request}
        )
        responce_data = product_serializer.data

        if not product_info.exists():
            responce_data["product_info"] = []
            return Response(responce_data, status=200)

        info_serializer = DetailProductSerializer(product)
        responce_data["product_info"] = info_serializer.data
        return Response(responce_data)
