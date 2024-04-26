from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Q

from drf_yasg.utils import swagger_auto_schema


from API.serializers.SearchSerializers import SearchSerializer
from API.serializers.MainProductSerializers import ProductSerializer
from backend.paginator import StandardResultsSetPagination
from DB.models import Product

# TODO)) Если поисковой запрос пустой, то что-то придумать надо будет


class GlobalSearch(APIView):
    # throttle_classes = [SearchThrottle] FIXME

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
