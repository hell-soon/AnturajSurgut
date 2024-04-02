from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order, Additionalservices, OrderFace, OrderType, PaymentType
from .serializers.OrderSerializers import OrderSerializer
from .serializers.OrderUpdateSerializers import UpdateOrderSerializer
from .serializers.OrderComponentSerializers import (
    OrderFaceSerializer,
    OrderTypeSerializer,
    PaymentTypeSerializer,
    AdditionalservicesSerializer,
    CombinedDataSerializer,
)


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
            description="Возвращается сообщение о том, что заказ не может быть обновлен, если его статус отличен От 'Не готов'",
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

    serializer = UpdateOrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=["get"],
    responses={
        200: openapi.Response(
            description="Список доступных услуг к заказу",
            schema=AdditionalservicesSerializer(),
        ),
    },
)
@api_view(["GET"])
def get_additional_services(request):
    additional_services = Additionalservices.objects.all()
    serializer = AdditionalservicesSerializer(additional_services, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    methods=["get"],
    responses={
        200: openapi.Response(
            description="Список типов заказов, типов лиц и типов оплат",
            schema=CombinedDataSerializer(),
        ),
    },
)
@api_view(["GET"])
def order_utils(request):
    order_types = OrderType.objects.all()
    order_faces = OrderFace.objects.all()
    payment_types = PaymentType.objects.all()

    # Сериализация данных
    order_type_serializer = OrderTypeSerializer(order_types, many=True)
    order_face_serializer = OrderFaceSerializer(order_faces, many=True)
    payment_type_serializer = PaymentTypeSerializer(payment_types, many=True)

    # Объединение данных в один словарь
    combined_data = {
        "order_type": order_type_serializer.data,
        "order_face": order_face_serializer.data,
        "payment_type": payment_type_serializer.data,
    }

    # Сериализация объединенных данных
    # combined_data_serializer = CombinedDataSerializer(combined_data)

    return Response(combined_data)
