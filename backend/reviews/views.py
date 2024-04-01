from django.shortcuts import render
from rest_framework import viewsets
from .serializers.ReviewsMainSerializers import ReviewSerializer
from .serializers.ReviewsChangeSerializers import ReviewChangeSerializer
from .models import Review
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from icecream import ic
from rest_framework import status


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ["get"]


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def review_create(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(
            user=request.user
        )  # Предполагается, что пользователь авторизован
        return Response(
            {"message": "Отзыв успешно опубликован"}, status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
