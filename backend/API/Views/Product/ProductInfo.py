from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from API.serializers.DetailProductSerializers import DetailProductSerializer
from DB.models import ProductInfo, Product


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
