from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Order
from DB.utils.codes import STATUS_MAP
from .serializers.OrderSerializers import OrderSerializer, UpdateOrderSerializer
from icecream import ic


@swagger_auto_schema(
    method="post",
    request_body=OrderSerializer,
    responses={
        201: openapi.Response(
            description="Заказ успешно создан",
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


@swagger_auto_schema(
    method="put",
    request_body=UpdateOrderSerializer,
    responses={
        200: openapi.Response(
            description="заказ успешно обновлен",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
        400: openapi.Response(
            description="Возвращается сообщение о том, что заказ не может быть обновлен, если его статус отличен от оличаеться От 'Не готов'",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
    },
)
@api_view(["PUT"])
def update_order(request, order_number):
    try:
        order = Order.objects.get(order_number=order_number)
    except Order.DoesNotExist:
        return Response({"error": "Заказ не найден"}, status=status.HTTP_404_NOT_FOUND)

    if order.order_status != "1":
        order_status = STATUS_MAP.get(order.order_status)
        return Response(
            {
                "error": f"Заказ не может быть обновлен, так как его статус {order_status}"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = UpdateOrderSerializer(instance=order, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Заказ успешно обновлен"}, status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
