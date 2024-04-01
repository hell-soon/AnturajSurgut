from django_filters import rest_framework as filters
from order.models import Order


class OrderFilter(filters.FilterSet):
    user_email = filters.CharFilter(field_name="user_email", lookup_expr="iexact")
    user_phone = filters.CharFilter(field_name="user_phone", lookup_expr="iexact")

    class Meta:
        model = Order
        fields = ["user_email", "user_phone"]
