from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserUpdatePasswordSerializer,
    UserEmailSerializer,
    OrderSerializer,
)
from rest_framework.permissions import IsAuthenticated

from users.models import CustomUser
from .tasks import send_link_for_change_pass
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


@api_view(["POST"])
def register_user(request):
    """
    Регистрация пользователя
    """
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    """
    Аутентификация пользователя
    """

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def email_for_change_pass(request):
    """
    Конечная точка для обработки запроса на отправку электронной почты для смены пароля.
    Эта функция принимает запрос POST и ожидает поле 'email' в данных запроса.
    Если электронная почта действительна, отправляется электронное письмо с ссылкой для изменения пароля.
    Если электронная почта не найдена в базе данных, возвращается ответ с ошибкой 400 и сообщением о том, что учетная запись с указанной электронной почтой не была найдена.
    Если данные запроса недопустимы, возвращается ответ с ошибкой 400 и ошибками сериализатора.
    """
    serializer = UserEmailSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get("email")
        try:
            user = CustomUser.objects.get(email=email)
            send_link_for_change_pass.delay(email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            return Response(
                {
                    "message": "На указанную почту было отправленно письмо",
                    "uid": uid,
                    "token": token,
                }
            )
        except CustomUser.DoesNotExist:
            return Response({"message": "Аккаунт с такой почтой не найден"}, status=400)
    else:
        return Response(serializer.errors, status=400)


@api_view(["POST"])
def change_password(request, uid64, token):
    """
    Функция для изменения пароля пользователя. Принимает объект запроса, uid64 и токен в качестве параметров и возвращает объект Response.
    """
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = CustomUser.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            serializer = UserUpdatePasswordSerializer(data=request.data)
            if serializer.is_valid():
                # Обновление пароля пользователя
                user.set_password(serializer.validated_data["password"])
                user.save()
                return Response(
                    {"message": "Пароль успешно обновлен"}, status=status.HTTP_200_OK
                )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"message": "Неверный токен для смены пароля"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        return Response(
            {"message": "Неверный идентификатор пользователя"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["POST"])
def create_order(request):
    if request.method == "POST":
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
