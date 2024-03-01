from django_filters import filters
from django_filters.rest_framework import FilterSet, CharFilter
from django.db.models import Q
from DB.models import Product, Tags, SubCatalog


class ProductFilter(FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name="tags__name", to_field_name="name", queryset=Tags.objects.all()
    )
    high_rating = filters.BooleanFilter(method="filter_high_rating")
    sub_catalog = filters.ModelChoiceFilter(queryset=SubCatalog.objects.all())

    class Meta:
        model = Product
        fields = ["tags", "created_at", "rating", "high_rating", "sub_catalog"]

    def filter_created_at(self, queryset, name, value):
        return queryset.filter(Q(created_at__lte=value) | Q(created_at__gte=value))

    def filter_rating(self, queryset, name, value):
        # This method will be used to filter products with high rating
        return self.filter_high_rating(queryset, name, value)

    def filter_high_rating(self, queryset, name, value):
        if value:
            # If the filter parameter is True, return products with highest rating
            return queryset.order_by("-rating")
        else:
            # If the filter parameter is False or not specified, return all products without changes
            return queryset
