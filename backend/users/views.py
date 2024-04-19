from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import CustomUser
from .tasks import send_link_for_change_pass
from .serializers.Register.UserRegister import UserRegisterSerializer
from .serializers.Login.UserLogin import UserLoginSerializer
from .serializers.Component.EmailSerializers import UserEmailSerializer
from .serializers.Update.UserPasswordUpdate import UserUpdatePasswordSerializer


@swagger_auto_schema(
    method="post",
    request_body=UserRegisterSerializer,
    responses={
        201: openapi.Response(
            description="Пользователь успешно создан",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
        400: openapi.Response(
            description="Запрос не прошел валидацию",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "email": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                    "error": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
            examples={
                "application/json": {
                    "email": ["Пользователь с таким email уже существует."],
                    "error": "Пароль должен быть не менее 8 символов.",
                }
            },
        ),
    },
)
@api_view(["POST"])
def register_user(request):
    """
    Регистрация пользователя
    """
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(
            {"message": "Пользователь успешно создан"}, status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="post",
    request_body=UserEmailSerializer,
    responses={
        200: openapi.Response(
            description="Письмо успешно отправлено",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "refresh": openapi.Schema(type=openapi.TYPE_STRING),
                    "access": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
        400: "Некорректные данные запроса",
    },
)
@api_view(["POST"])
def user_login_view(request):
    """
    Аутентификация пользователя
    """
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


@swagger_auto_schema(
    method="post",
    request_body=UserEmailSerializer,
    responses={
        200: openapi.Response(
            description="Письмо успешно отправлено",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                    "uid": openapi.Schema(type=openapi.TYPE_STRING),
                    "token": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
        400: "Некорректные данные запроса",
    },
)
@api_view(["POST"])
def email_for_change_pass(request):
    serializer = UserEmailSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get("email")
        try:
            user = CustomUser.objects.get(email=email).exists()
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


@swagger_auto_schema(
    method="post",
    request_body=UserUpdatePasswordSerializer,
    manual_parameters=[
        openapi.Parameter(
            "token",
            openapi.IN_PATH,
            description="Токен для смены пароля",
            type=openapi.TYPE_STRING,
        ),
    ],
    responses={
        200: "Пароль успешно обновлен",
        400: "Неверный токен для смены пароля или идентификатор пользователя",
    },
)
@api_view(["POST"])
def change_password(request, uidb64, token):
    """
    Endpoint для окончательной смены пароля пользователя.
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            serializer = UserUpdatePasswordSerializer(data=request.data)
            if serializer.is_valid():
                # Обновление пароля пользователя
                user.set_password(serializer.validated_data["password1"])
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
