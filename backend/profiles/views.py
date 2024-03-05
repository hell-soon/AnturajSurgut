from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import IntegrityError
from .serializers import UserSerializer, ChangeUserInfo
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response(
            description="Пользователь успешно получен",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={"user": openapi.Schema(type=openapi.TYPE_OBJECT)},
            ),
        ),
    },
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_info(request):
    """
    Представление API для вывода информации о пользователе
    """
    user = request.user
    return Response({"user": UserSerializer(user).data})


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
def change_info(request):
    """
    Представление API для изменения информации о пользователе
    """
    user = request.user
    serializer = ChangeUserInfo(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Данные успешно изменены!"})
    return Response(serializer.errors)
