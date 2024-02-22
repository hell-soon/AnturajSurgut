from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method="post",
    request_body=OrderSerializer,
    responses={
        201: openapi.Response(
            description="Пользователь успешно создан",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                    "order_number": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
        400: "Возвращается ответ с ошибкой 400 и ошибками сериализатора",
    },
)
@api_view(["POST"])
def create_order(request):
    """
    Create a new order.

    Parameters:
    - order_data (object): The data for the new order.

    Returns:
    - data (object): The data of the created order.
    """
    if request.method == "POST":
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Заказ успешно создан",
                    "order_number": serializer.data["order_number"],
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
