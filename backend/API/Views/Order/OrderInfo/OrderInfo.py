from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from order.models import Order
from order.serializers.OrderSerializers import OrderSerializer


class OrderInfoView(APIView):
    def get(self, request, order_number):
        order = Order.objects.get(order_number=order_number)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
