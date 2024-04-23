from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializers.vacancyserializer import VacancySerializer, BaseVacancySerializer
from .Serializers.vacancyresponse import VacancyResponseSerializer
from .models import Vacancy
from API.Utils.Paginator.PaginationClass import StandardResultsSetPagination


class VacancyView(APIView):
    queryset = Vacancy.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = VacancySerializer
    permission_classes = [AllowAny, IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return VacancyResponseSerializer
        return self.serializer_class

    def post(self, request):
        if request.user.is_authenticated:
            serializer = self.get_serializer_class()
            serializer = serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response(
                {
                    "message": "Спасибо за ваш отклик, мы свяжемся с вами в ближайшее время!"
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"detail": "Учетные данные не были предоставлены."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    def get(self, request):
        return Response({"success": "GET"})
