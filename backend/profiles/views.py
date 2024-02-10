from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from database.models import Favorite
from django.db import IntegrityError


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_info(request):
    """_summary_
    Представление API для вывода информации о пользователе
    Returns:
        _type_: _description_
    """
    user = request.user
    return Response(
        {
            "phone": user.phone,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
    )


@api_view(["POST"])
def add_to_favorite(request):
    """
    Представление API для добавления товара в избранное
    """
    user = request.user
    product_id = request.data.get("product_id")

    if not product_id:
        return Response({"error": "Не указан ID продукта"}, status=400)

    try:
        favorite = Favorite.objects.create(user=user, product_id=product_id)
        return Response({"success": "Товар добавлен в избранное"})

    except IntegrityError:
        return Response({"error": "Такого продукта нет в базе данных"})

    except Exception as e:
        return Response({"error": str(e)})

    """
    НЕЛЬЗЯ ДОБАВЛЯТЬ ОДИН И ТОТ ЖЕ ТОВАР, КОТОРЫЙ ЕСТЬ В ИЗБРАННОМ ДОБАВИТЬ ОБРАБОТЧИК
    """

    """
    Предствалнеине API для удаления товара из избранного
    """
