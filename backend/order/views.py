from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer


@api_view(["POST"])
def create_order(request):
    """
    Create a new order.

    Parameters:
    - order_data (object): The data for the new order.

    Returns:
    - data (object): The data of the created order.
    """
    if request.method == "POST":
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Заказ успешно создан",
                    "order_number": serializer.data["order_number"],
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
