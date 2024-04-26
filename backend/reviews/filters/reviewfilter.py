from django_filters import filters
from django_filters.rest_framework import FilterSet

from reviews.models import Review


class ReviewsFilter(FilterSet):
    high_rating = filters.BooleanFilter(
        method="filter_high_rating", field_name="rating", label="По рейтингу(Boolean)"
    )
    text = filters.CharFilter(
        field_name="text",
        lookup_expr="icontains",
        max_length=50,
    )
    created = filters.DateFilter(lookup_expr="gte", field_name="created_at")

    class Meta:
        model = Review
        fields = ["high_rating"]

    def filter_high_rating(self, queryset, name, value):
        if value:
            return queryset.order_by("-rating")
        return queryset
