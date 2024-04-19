from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from API.serializers.DetailProductSerializers import DetailProductSerializer
from API.serializers.MainProductSerializers import ProductSerializer
from DB.models import ProductInfo, Product


class ProductInfoView(APIView):

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="Информация о товаре",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "product": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                "name": openapi.Schema(type=openapi.TYPE_STRING),
                                "description": openapi.Schema(type=openapi.TYPE_STRING),
                                "image": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(
                                        type=openapi.TYPE_OBJECT,
                                        properties={
                                            "image": openapi.Schema(
                                                type=openapi.TYPE_STRING
                                            )
                                        },
                                    ),
                                ),
                                "catalog": openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                        "name": openapi.Schema(
                                            type=openapi.TYPE_STRING
                                        ),
                                        "image": openapi.Schema(
                                            type=openapi.TYPE_STRING
                                        ),
                                        "subcatalog": openapi.Schema(
                                            type=openapi.TYPE_OBJECT,
                                            properties={
                                                "id": openapi.Schema(
                                                    type=openapi.TYPE_INTEGER
                                                ),
                                                "name": openapi.Schema(
                                                    type=openapi.TYPE_STRING
                                                ),
                                                "image": openapi.Schema(
                                                    type=openapi.TYPE_STRING
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "tags": openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(
                                        type=openapi.TYPE_OBJECT,
                                        properties={
                                            "id": openapi.Schema(
                                                type=openapi.TYPE_INTEGER
                                            ),
                                            "name": openapi.Schema(
                                                type=openapi.TYPE_STRING
                                            ),
                                        },
                                    ),
                                ),
                                "created_at": openapi.Schema(type=openapi.TYPE_STRING),
                            },
                        ),
                        "product_info": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "product_info_id": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "color": openapi.Schema(
                                        type=openapi.TYPE_OBJECT,
                                        properties={
                                            "name": openapi.Schema(
                                                type=openapi.TYPE_STRING
                                            ),
                                            "color": openapi.Schema(
                                                type=openapi.TYPE_STRING
                                            ),
                                        },
                                    ),
                                    "size": openapi.Schema(
                                        type=openapi.TYPE_OBJECT,
                                        properties={
                                            "name": openapi.Schema(
                                                type=openapi.TYPE_STRING
                                            )
                                        },
                                    ),
                                    "quantity": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                    "cost": openapi.Schema(type=openapi.TYPE_INTEGER),
                                    "promotion": openapi.Schema(
                                        type=openapi.TYPE_BOOLEAN
                                    ),
                                    "promotion_cost": openapi.Schema(
                                        type=openapi.TYPE_INTEGER
                                    ),
                                },
                            ),
                        ),
                    },
                ),
            ),
        },
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
