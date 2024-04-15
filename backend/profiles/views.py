from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.views import APIView
from .serializers.Update.UserUpd import UserUpdateSerializer
from .serializers.Users.UserSerializer import UserSerializer
from users.models import CustomUser
from order.models import Order
from DB.utils.codes import STATUS_MAP
from django.db.models import Q

from icecream import ic


@swagger_auto_schema(
    method="patch",
    request_body=UserSerializer,
    responses={
        200: openapi.Response(
            description="Пользователь успешно изменен",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={"message": openapi.Schema(type=openapi.TYPE_STRING)},
            ),
        )
    },
)
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_user_view(request):
    user = request.user
    serializer = UserUpdateSerializer(instance=user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_user_order(user):
    orders = Order.objects.filter(Q(user_email=user.email) | Q(user_phone=user.phone))
    order_list = []
    if orders:
        for order in orders:
            order_dict = {}
            order_dict["order_number"] = order.order_number
            order_dict["order_status"] = STATUS_MAP[order.order_status]
            order_dict["created_at"] = order.created_at.strftime("%d.%m.%Y" + " %H:%M")
            order_list.append(order_dict)
        return order_list
    return None


@api_view(["POST"])
def tg_order_buttons(request):
    try:
        user = CustomUser.objects.get(user_tg_id=request.data.get("tg_id"))
        orders = get_user_order(user)
    except CustomUser.DoesNotExist:
        return Response({"orders": None})
    return Response({"orders": orders})


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]

    def get(self, request):
        user = request.user
        user_orders = request.query_params.get("user_orders", "false").lower() == "true"
        serializer = UserSerializer(user)
        data = serializer.data

        if user_orders:
            data["orders"] = get_user_order(user)

        return Response(data)
