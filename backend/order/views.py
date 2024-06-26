from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Order,
    Additionalservices,
    OrderFace,
    OrderType,
    PaymentType,
    OrderStatus,
)
from .serializers.OrderSerializers import OrderSerializer
from .serializers.OrderUpdateSerializers import UpdateOrderSerializer
from .serializers.OrderComponentSerializers import (
    OrderFaceSerializer,
    OrderTypeSerializer,
    PaymentTypeSerializer,
    AdditionalservicesSerializer,
    OrderUtilsSerializer,
)
from icecream import ic
from .Payment.Online.create import create_online_check
from backend.schema.errors import generate_error_schema


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
                    "payment_url": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
        400: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=generate_error_schema(OrderSerializer),
        ),
    },
)
@api_view(["POST"])
def create_order(request):  #
    serializer = OrderSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    order = serializer.save()

    response_data = {
        "message": "Заказ успешно создан",
        "order_number": order.id,
    }

    if order.payment_type.name == "Онлайн оплата":
        payment = create_online_check(order)
        order.payment_id = payment.id
        order.save()
        response_data["payment_url"] = payment.confirmation.confirmation_url

    return Response(response_data, status=status.HTTP_201_CREATED)


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
            schema=OrderUtilsSerializer(),
        ),
    },
)
@api_view(["GET"])
def order_utils(request):
    data = {
        "order_type": OrderType.objects.all(),
        "order_face": OrderFace.objects.all(),
        "payment_type": PaymentType.objects.all(),
        "order_status": OrderStatus.objects.all(),
    }
    serializer = OrderUtilsSerializer(data)
    return Response(serializer.data)
