from django_filters import filters
from django_filters.rest_framework import FilterSet, CharFilter
from django.db.models import Q
from DB.models import Product, Tags


class ProductFilter(FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name="tags__name", to_field_name="name", queryset=Tags.objects.all()
    )
    high_rating = filters.BooleanFilter(method="filter_high_rating")

    class Meta:
        model = Product
        fields = ["tags", "created_at", "rating", "high_rating"]

    def filter_created_at(self, queryset, name, value):
        return queryset.filter(Q(created_at__lte=value) | Q(created_at__gte=value))

    def filter_rating(self, queryset, name, value):
        # Этот метод теперь будет использоваться для фильтрации товаров с высоким рейтингом
        return self.filter_high_rating(queryset, name, value)

    def filter_high_rating(self, queryset, name, value):
        if value:
            # Если параметр фильтра равен True, то возвращаем товары с наиболее высоким рейтингом
            return queryset.order_by("-rating")
        else:
            # Если параметр фильтра равен False или не указан, то возвращаем все товары без изменений
            return queryset
