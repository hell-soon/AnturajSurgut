from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from API.serializers.DetailProductSerializers import DetailProductSerializer
from API.serializers.MainProductSerializers import ProductSerializer
from API.serializers.SchemasSerializers import SchemaInfoProductSerializer
from DB.models import ProductInfo, Product


class ProductInfoView(APIView):
    @swagger_auto_schema(
        responses={200: SchemaInfoProductSerializer, 404: "Товар не найден"},
    )
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
                    responce_data = {}
                    info_serializer = DetailProductSerializer(product_info, many=True)
                    product_serializer = ProductSerializer(product)
                    responce_data = product_serializer.data
                    responce_data["product_info"] = info_serializer.data
                    return Response(responce_data)
                else:
                    return Response("Товара нет в наличии")
        except Product.DoesNotExist:
            raise NotFound("Товар не найден")
