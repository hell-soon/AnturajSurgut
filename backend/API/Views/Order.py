from rest_framework import viewsets
from django_filters import rest_framework as filters
from order.models import Order
from order.serializers.OrderSerializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ["get"]
