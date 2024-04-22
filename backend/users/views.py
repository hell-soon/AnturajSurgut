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
                    "first_name": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                    "last_name": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                    "email": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                    "password": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                    "password_repeat": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                    "error": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                },
            ),
        ),
    },
)
@api_view(["POST"])
def register_user(request):
    """
    Регистрация пользователя
    """
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
        {"message": "Пользователь успешно создан"}, status=status.HTTP_201_CREATED
    )


@swagger_auto_schema(
    method="post",
    request_body=UserLoginSerializer,
    responses={
        200: openapi.Response(
            description="Успешная аутентификация",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "refresh": openapi.Schema(type=openapi.TYPE_STRING),
                    "access": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
        400: openapi.Response(
            description="Некорректные данные запроса",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "email": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                    "password": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                    "error": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                },
            ),
        ),
    },
)
@api_view(["POST"])
def user_login_view(request):
    """
    Аутентификация пользователя
    """
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    refresh = RefreshToken.for_user(user)
    return Response(
        {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
    )


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
                    "uidb64": openapi.Schema(type=openapi.TYPE_STRING),
                    "token": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
        400: openapi.Response(
            description="Некорректные данные запроса",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "email": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                },
            ),
            examples={
                "application/json": {
                    "email": ["Пользователь с таким email не существует."],
                }
            },
        ),
    },
)
@api_view(["POST"])
# NEED CHECK MAYBE CAN BE BROKEN TODO))
def email_for_change_pass(request):
    """Точка проверяет существования пользователя, если существует то отправляет письмо с ссылкой для смены пароля, а в ответ передает параметры для следуйщего шага"""
    serializer = UserEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data.get("email")
    user = CustomUser.objects.get(email=email)

    send_link_for_change_pass.delay(email)
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    return Response(
        {
            "message": "На указанную почту было отправленно письмо",
            "uidb64": uidb64,
            "token": token,
        }
    )


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
        200: openapi.Response(
            description="Пароль успешно обновлен",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "message": openapi.Schema(type=openapi.TYPE_STRING)
                        },
                    ),
                },
            ),
        ),
        400: openapi.Response(
            description="Некорректные данные запроса",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "password": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                    "password_repeat": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                    "error": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    ),
                },
            ),
        ),
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
            serializer.is_valid(raise_exception=True)
            user.set_password(serializer.validated_data["password"])
            user.save()
            return Response(
                {"message": "Пароль успешно обновлен"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": ["Неверный токен для смены пароля"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        return Response(
            {
                "error": [
                    "Произошла критическая ошибка, попробуйте ещё раз или свяжитесь с администратором"
                ]
            },
            status=status.HTTP_400_BAD_REQUEST,
        )



