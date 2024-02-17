from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from database.models import Favorite
from django.db import IntegrityError
from .serializers import UserSerializer
from rest_framework import generics


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_info(request):
    """
    Представление API для вывода информации о пользователе
    """
    user = request.user
    favorite = Favorite.objects.filter(user=user)
    favorite_list = [{"product_id": favorite.product.id} for favorite in favorite]
    return Response(
        {
            "user": UserSerializer(user).data,
            "favorites": favorite_list,
        }
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_favorite(request):
    user = request.user
    product_id = request.data.get("product_id")

    if not product_id:
        return Response({"error": "Не указан ID продукта"}, status=400)

    try:
        if Favorite.objects.filter(user=user, product_id=product_id).exists():
            return Response({"error": "Такой продукт уже есть в избранном"})

        New_favorite = Favorite.objects.create(user=user, product_id=product_id)
        return Response({"success": "Товар добавлен в избранное"})

    except IntegrityError:
        return Response({"error": "Такого продукта нет в базе данных"})

    except Exception as e:
        return Response({"error": str(e)})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_from_favorite(request):
    user = request.user
    product_id = request.data.get("product_id")

    if not product_id:
        return Response({"error": "Не указан ID продукта"}, status=400)

    try:
        favorite_item = Favorite.objects.get(user=user, product_id=product_id)
        favorite_item.delete()
        return Response({"success": "Товар удален из избранного"})

    except Favorite.DoesNotExist:
        return Response({"error": "Такого продукта нет в избранном"})
