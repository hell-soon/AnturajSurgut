from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .Serializers.vacancyserializer import VacancySerializer, BaseVacancySerializer
from .Serializers.vacancyresponse import VacancyResponseSerializer
from .models import Vacancy, ResponseVacancy
from backend.paginator import StandardResultsSetPagination
from rest_framework.decorators import action, permission_classes


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = VacancySerializer
    http_method_names = ["get", "post"]
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BaseVacancySerializer
        return super().get_serializer_class()

    @action(detail=True, methods=["post"])
    @permission_classes([IsAuthenticated])
    def respond(self, request, pk=None):
        if request.user.is_authenticated:
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
        else:
            return Response(
                {"detail": "Учетные данные не были предоставлены"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
