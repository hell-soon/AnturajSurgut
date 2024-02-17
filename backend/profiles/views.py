from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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
    return Response({"user": UserSerializer(user).data})
