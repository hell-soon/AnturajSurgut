from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Q

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from API.serializers.SearchSerializers import SearchSerializer
from API.serializers.ProductSerializers import ProductSerializer
from API.serializers.Schemas import ProductPaginationSerializer
from backend.paginator import StandardResultsSetPagination
from backend.schema.errors import generate_error_schema
from DB.models import Product

# TODO)) Если поисковой запрос пустой, то что-то придумать надо будет


class GlobalSearch(APIView):
    # throttle_classes = [SearchThrottle] FIXME

    @swagger_auto_schema(
        request_body=SearchSerializer,
        responses={
            200: ProductPaginationSerializer(many=True),
            400: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=generate_error_schema(SearchSerializer),
            ),
        },
    )
    def post(self, request):
        search_serializer = SearchSerializer(data=request.data)
        search_serializer.is_valid(raise_exception=True)
        search_data = search_serializer.data.get("search_data")
        products = (
            Product.objects.filter(product_status=True).filter(
                Q(name__icontains=search_data) | Q(description__icontains=search_data)
            )
        ).order_by("-created_at")
        paginator = StandardResultsSetPagination()
        page = paginator.paginate_queryset(products, request)
        serialized_products = ProductSerializer(page, many=True)
        return paginator.get_paginated_response(serialized_products.data)
