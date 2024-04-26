from django_filters import ModelMultipleChoiceFilter
from django_filters.rest_framework import FilterSet


from order.models import Order, OrderStatus


class OrderFilter(FilterSet):
    status = ModelMultipleChoiceFilter(
        queryset=OrderStatus.objects.all(),
        label="По статусу",
        method="filter_status",
    )

    class Meta:
        model = Order
        fields = ["created_at", "status"]

    def filter_status(self, queryset, name, value):
        if value:
            return queryset.filter(order_status__in=value)
        return queryset
