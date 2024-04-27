from rest_framework import status
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from backend.paginator import StandardResultsSetPagination
from backend.schema.errors import generate_error_schema

from .serializers.ReviewsMainSerializers import ReviewSerializer
from .serializers.FeedbackSerializers import FeedBackSerializer

from .models import Review


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by("-created_at")
    serializer_class = ReviewSerializer
    http_method_names = ["get"]
    pagination_class = StandardResultsSetPagination
    permission_classes = [AllowAny]


@swagger_auto_schema(
    method="post",
    request_body=FeedBackSerializer,
    responses={
        201: openapi.Response(
            "message",
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={"message": openapi.Schema(type=openapi.TYPE_STRING)},
            ),
        ),
        400: openapi.Response(
            "Ошибки валидации",
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=generate_error_schema(FeedBackSerializer),
            ),
        ),
    },
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
