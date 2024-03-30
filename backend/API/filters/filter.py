from django_filters import filters
from django_filters.rest_framework import FilterSet, CharFilter
from django.db.models import Q
from DB.models import Product, Tags, SubCatalog
from icecream import ic


class ProductFilter(FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name="tags", to_field_name="id", queryset=Tags.objects.all()
    )
    high_rating = filters.BooleanFilter(
        method="filter_high_rating", field_name="По рейтингу", label="По рейтингу"
    )
    sub_catalog = filters.ModelChoiceFilter(queryset=SubCatalog.objects.all())

    class Meta:
        model = Product
        fields = ["tags", "created_at", "high_rating", "sub_catalog"]

    def filter_high_rating(self, queryset, name, value):
        if value:
            # If the filter parameter is True, return products with highest rating
            return queryset.order_by("-rating")
        else:
            # If the filter parameter is False or not specified, return all products without changes
            return queryset

    filter_high_rating.short_description = "По рейтингу"
