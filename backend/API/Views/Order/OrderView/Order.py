from rest_framework import viewsets
from django_filters import rest_framework as filters
from order.models import Order
from order.serializers.OrderSerializers import OrderSerializer
from API.filters.OrderFilter import OrderFilter


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ["get"]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = OrderFilter
