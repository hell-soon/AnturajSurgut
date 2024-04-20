from rest_framework import viewsets
from rest_framework.views import APIView
from django.db.models import Q
from django_filters import rest_framework as filters

from rest_framework.response import Response
from DB.models import Product

from API.serializers.MainProductSerializers import ProductSerializer
from API.serializers.SearchSerializers import SearchSerializer
from API.filters.ProductFilter import ProductFilter

from API.Utils.Paginator.PaginationClass import StandardResultsSetPagination

from drf_yasg.utils import swagger_auto_schema


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(product_status=True).order_by(
        "name", "-created_at"
    )
    serializer_class = ProductSerializer
    http_method_names = ["get"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilter
    pagination_class = StandardResultsSetPagination


# TODO)) Если поисковой запрос пустой, то что-то придумать надо будет
class GlobalSearch(APIView):
    @swagger_auto_schema(
        request_body=SearchSerializer, responses={200: ProductSerializer(many=True)}
    )
    def post(self, request):
        search_serializer = SearchSerializer(data=request.data)
        if search_serializer.is_valid(raise_exception=True):
            search_data = search_serializer.data.get("search_data")
            products = (
                Product.objects.filter(product_status=True).filter(
                    Q(name__icontains=search_data)
                    | Q(description__icontains=search_data)
                )
            ).order_by("-created_at")
            paginator = StandardResultsSetPagination()
            page = paginator.paginate_queryset(products, request)
            serialized_products = ProductSerializer(page, many=True)
            return paginator.get_paginated_response(serialized_products.data)
        return Response(search_serializer.errors, status=400)
