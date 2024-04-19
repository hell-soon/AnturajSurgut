from rest_framework import status
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination


from .serializers.Schemas import (
    SchemaRewiewCreateSerializer,
    AuthShema,
    SuccessSerializer,
)
from .serializers.ReviewsMainSerializers import ReviewSerializer
from .serializers.ReviewsChangeSerializers import ReviewChangeSerializer
from .serializers.FeedbackSerializers import FeedBackSerializer
from .models import Review

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by("-created_at")
    serializer_class = ReviewSerializer
    http_method_names = ["get"]
    pagination_class = StandardResultsSetPagination


@swagger_auto_schema(
    method="post",
    # request_body=SchemaRewiewCreateSerializer,
    responses={
        201: openapi.Response(
            description="Отзыв успешно опубликован", schema=SuccessSerializer()
        ),
        400: openapi.Response(
            description="Некорректные данные",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "field_name": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                    )
                },
            ),
        ),
        401: AuthShema.schema(),
    },
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def review_create(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(
            {"message": "Отзыв успешно опубликован"}, status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="put",
    request_body=SchemaRewiewCreateSerializer,
    responses={
        200: openapi.Response(description="Отзыв обновлен", schema=ReviewSerializer()),
        401: AuthShema.schema(),
        403: openapi.Response(
            description="Вы не можете изменить этот отзыв",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={"error": openapi.Schema(type=openapi.TYPE_STRING)},
            ),
        ),
        404: openapi.Response(
            description="Отзыв не найден",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={"error": openapi.Schema(type=openapi.TYPE_STRING)},
            ),
        ),
    },
)
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_review(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response({"error": "Отзыв не найден"}, status=status.HTTP_404_NOT_FOUND)

    if review.user != request.user:
        return Response(
            {"error": "Вы не можете изменить этот отзыв"},
            status=status.HTTP_403_FORBIDDEN,
        )

    serializer = ReviewChangeSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_review(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response({"error": "Отзыв не найден"}, status=status.HTTP_404_NOT_FOUND)

    if review.user != request.user:
        return Response(
            {"error": "Вы не можете удалить этот отзыв"},
            status=status.HTTP_403_FORBIDDEN,
        )

    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def feedback(request):
    serializer = FeedBackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            status=status.HTTP_201_CREATED,
            data={"message": "Мы с вами свяжемся в ближайшее время"},
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
