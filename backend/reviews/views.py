from rest_framework import status
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.paginator import StandardResultsSetPagination

from .serializers.ReviewsMainSerializers import ReviewSerializer
from .serializers.ReviewsChangeSerializers import ReviewChangeSerializer
from .serializers.FeedbackSerializers import FeedBackSerializer
from .models import Review


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by("-created_at")
    serializer_class = ReviewSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    pagination_class = StandardResultsSetPagination
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.action == "update":
            return ReviewChangeSerializer
        return ReviewSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Отзыв успешно опубликован"},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        if instance.user != request.user:
            return Response(
                {"detail": "У вас нет разрешения на изменение этого отзыва"},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {"message": "Отзыв успешно обновлен"}, status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response(
                {"detail": "У вас нет разрешения на удаление этого отзыва"},
                status=status.HTTP_403_FORBIDDEN,
            )
        self.perform_destroy(instance)
        return Response(
            {"message": "Отзыв успешно удален"}, status=status.HTTP_204_NO_CONTENT
        )


@api_view(["POST"])
# @throttle_classes([FeedbackThrottle]) FIXME THROTTLE
def feedback(request):
    serializer = FeedBackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            status=status.HTTP_201_CREATED,
            data={"message": "Мы с вами свяжемся в ближайшее время"},
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
