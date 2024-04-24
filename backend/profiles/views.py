from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from users.models import CustomUser

from .serializers.Update.UserUpd import UserUpdateSerializer
from .serializers.Users.UserSerializer import UserSerializer

from .misc.search_orders import get_user_order


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
# @throttle_classes([UserRateThrottle]) FIXME
def update_user_view(request):
    user = request.user
    serializer = UserUpdateSerializer(instance=user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def tg_order_buttons(request):
    try:
        user = CustomUser.objects.get(tg_id=request.data.get("tg_id"))
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
            print("sadsad")
            data["orders"] = get_user_order(user)

        return Response(data)
