from django_filters import filters, ModelMultipleChoiceFilter
from django_filters.rest_framework import FilterSet

from django.db.models import Q

from DB.models import Product, Tags, SubCatalog, Compound, Color, Size


class ProductFilter(FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name="tags", to_field_name="id", queryset=Tags.objects.all()
    )
    high_rating = filters.BooleanFilter(
        method="filter_high_rating", field_name="rating", label="По рейтингу(Boolean)"
    )
    created_at = filters.DateFilter(lookup_expr="gte")
    catalog_id = filters.NumberFilter(
        method="filter_catalog_id", label="По подкаталогу"
    )
    compound_id = ModelMultipleChoiceFilter(
        queryset=Compound.objects.all(), method="filter_compounds", label="По материалу"
    )
    subcatalog_id = ModelMultipleChoiceFilter(
        queryset=SubCatalog.objects.all(),
        method="filter_sub_catalog_id",
        label="По подкаталогу",
        required=False,
    )
    price = filters.RangeFilter(method="filter_price", label="По цене")
    color_id = ModelMultipleChoiceFilter(
        queryset=Color.objects.all(),
        method="filter_color",
        label="По цвету",
        required=False,
    )
    size_id = ModelMultipleChoiceFilter(
        queryset=Size.objects.all(),
        method="filter_size",
        label="По размеру",
        required=False,
    )
    most_sold = filters.BooleanFilter(
        method="filter_most_sold", label="По популярности"
    )

    class Meta:
        model = Product
        fields = [
            "tags",
            "created_at",
            "high_rating",
            "catalog_id",
            "compound_id",
            "price",
            "color_id",
            "size_id",
        ]

    def filter_most_sold(self, queryset, name, value):
        if value:
            return queryset.order_by("-total_sales")
        return queryset

    # ФИЛЬТР ПО КАТАЛОГУ
    def filter_catalog_id(self, queryset, name, value):
        if not value:
            return queryset

        return queryset.filter(sub_catalog__catalog__id=value).order_by("?")

    # ФИЛЬТР ПО ЦЕНОВОМУ ДИАПАЗОНУ
    def filter_price(self, queryset, name, value):
        if value:
            min_price = value.start
            max_price = value.stop
            price_filter = Q(
                productinfo__promotion_cost__gte=min_price,
                productinfo__promotion_cost__lte=max_price,
            ) | Q(productinfo__cost__gte=min_price, productinfo__cost__lte=max_price)
            queryset = queryset.filter(price_filter).order_by("-created_at").distinct()
            return queryset
        return queryset

    # ФИЛЬТР ПО МАТЕРИАЛУ
    def filter_compounds(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(compound__in=value)

    # Фильтрация по подкаталогу
    def filter_sub_catalog_id(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(sub_catalog__in=value)

    def filter_color(self, queryset, name, value):
        if value:
            return queryset.filter(productinfo__color__in=value)
        return queryset

    def filter_size(self, queryset, name, value):
        if value:
            return queryset.filter(productinfo__size__in=value)
        return queryset

    # ФИЛЬТР ПО РЕЙТИНГУ
    def filter_high_rating(self, queryset, name, value):
        if value:
            return queryset.order_by("-rating")
        return queryset


"""
СДЕЛАНЫЕ ФИЛЬТРЫ:

КАТАЛОГИ
ПОДКАТАЛОГИ
ТЭГИ
РЕЙТИНГ
СОСТАВ
ЦЕНА
НОВЫЕ ТОВАРЫ
ЦВЕТА
РАЗМЕРЫ

НАДО СДЕЛАТЬ:
ЧАСТО ПРОДОВАЕМЫЙ ТОВАР
"""
