from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.decorators import action

from django_filters import rest_framework as filters


from API.serializers.MainProductSerializers import ProductSerializer
from API.filters.ProductFilter import ProductFilter
from backend.paginator import StandardResultsSetPagination
from API.serializers.DetailProductSerializers import DetailProductSerializer
from DB.models import Product, ProductInfo


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(product_status=True).order_by("?")
    serializer_class = ProductSerializer
    http_method_names = ["get"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilter
    pagination_class = StandardResultsSetPagination

    @action(detail=True, methods=["get"])
    def info(self, request, pk=None):
        product = self.get_object()
        product_info = ProductInfo.objects.filter(product_id=product.id)
        if not product_info.exists():
            return Response("Информация о товаре не найдена")
        if not product.product_status:
            return Response("Товар отключен")

        responce_data = {}
        info_serializer = DetailProductSerializer(product_info, many=True)
        product_serializer = self.get_serializer_class()(
            product, context={"request": request}
        )
        responce_data = product_serializer.data
        responce_data["product_info"] = info_serializer.data
        return Response(responce_data)
