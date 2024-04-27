from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .Serializers.vacancyserializer import VacancySerializer, BaseVacancySerializer
from .Serializers.vacancyresponse import VacancyResponseSerializer
from .models import Vacancy, ResponseVacancy
from backend.paginator import StandardResultsSetPagination
from backend.schema.errors import generate_error_schema
from rest_framework.decorators import action, permission_classes

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = VacancySerializer
    http_method_names = ["get", "post"]
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.action == "respond":
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BaseVacancySerializer
        return super().get_serializer_class()

    @swagger_auto_schema(
        methods=["post"],
        request_body=VacancyResponseSerializer,
        responses={
            201: openapi.Response(
                description="Отклик успешно отправлен",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "message": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Сообщение об успешном отклике",
                        ),
                    },
                ),
            ),
            400: openapi.Response(
                "Ошибки валидации",
                openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties=generate_error_schema(VacancyResponseSerializer),
                ),
            ),
        },
    )
    @action(detail=True, methods=["post"])
    def respond(self, request, pk=None):
        vacancy = self.get_object()

        if not ResponseVacancy.objects.filter(
            vacancy=vacancy, user=request.user
        ).exists():
            serializer = VacancyResponseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(vacancy=vacancy, user=request.user)
            return Response(
                {
                    "message": "Спасибо за ваш отклик! Мы свяжемся с вами в ближайшее время!"
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"detail": "Пользователь уже откликнулся на эту вакансию"},
                status=status.HTTP_400_BAD_REQUEST,
            )
