from django.db.models import Q
from django_filters import rest_framework as filters

from DB.models import Tags, Product


class ProductFilter(filters.FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name="tags__name", to_field_name="name", queryset=Tags.objects.all()
    )

    class Meta:
        model = Product
        fields = ["tags", "created_at", "rating"]

    def filter_created_at(self, queryset, name, value):
        # Здесь вы можете определить логику фильтрации по дате создания
        # Например, если вы хотите получить только новые и старые продукты,
        # вы можете использовать Q-объекты для фильтрации по дате
        return queryset.filter(Q(created_at__lte=value) | Q(created_at__gte=value))
