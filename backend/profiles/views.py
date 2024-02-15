from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from database.models import Favorite, Cart, CartItem, Product
from django.db import IntegrityError
from .serializers import CartSerializer, UserSerializer
from rest_framework import generics


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_info(request):
    """
    Представление API для вывода информации о пользователе
    """
    user = request.user
    cart_id = user.cart.id
    favorite = Favorite.objects.filter(user=user)
    favorite_list = [{"product_id": favorite.product.id} for favorite in favorite]
    return Response(
        {
            "user": UserSerializer(user).data,
            "user_cart_id": cart_id,
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


@permission_classes([IsAuthenticated])
class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    user = request.user
    product_id = request.data.get("product_id")
    quantity = request.data.get("quantity", 1)  # По умолчанию 1, если не указано

    if not product_id:
        return Response({"error": "Не указан ID продукта"}, status=400)

    try:
        product = Product.objects.get(id=product_id)
        CartItem.add_to_cart(user.cart, product, quantity)
        return Response({"success": "Товар добавлен в корзину"})

    except Product.DoesNotExist:
        return Response({"error": "Такого продукта нет в базе данных"})

    except Exception as e:
        return Response({"error": str(e)})
