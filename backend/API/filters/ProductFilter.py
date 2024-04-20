from django_filters import filters
from django_filters.rest_framework import FilterSet, CharFilter
from django.db.models import Q
from DB.models import Product, Tags, SubCatalog
from icecream import ic
import random


class ProductFilter(FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name="tags", to_field_name="id", queryset=Tags.objects.all()
    )
    high_rating = filters.BooleanFilter(
        method="filter_high_rating", field_name="rating", label="По рейтингу(Boolean)"
    )
    sub_catalog = filters.ModelChoiceFilter(queryset=SubCatalog.objects.all())
    created_at = filters.DateFilter(lookup_expr="gte")
    catalog_id = filters.NumberFilter(
        method="filter_catalog_id", label="По подкаталогу"
    )
    catalog_id_slider = filters.NumberFilter(
        method="filter_catalog_id_slider", label="По подкаталогу для слайдера"
    )

    class Meta:
        model = Product
        fields = [
            "tags",
            "created_at",
            "high_rating",
            "sub_catalog",
            "catalog_id_slider",
        ]

    def filter_high_rating(self, queryset, name, value):
        if value:
            return queryset.order_by("-rating")
        else:
            return queryset

    def filter_catalog_id(self, queryset, name, value):
        while True:
            sub_catalog = SubCatalog.objects.filter(catalog_id=value)
            if sub_catalog:
                current_sub_catalog = random.choice(sub_catalog)
                products = Product.objects.filter(sub_catalog=current_sub_catalog)
                if products.count() >= 3:
                    random_products = random.sample(list(products), 3)
                    return queryset.filter(
                        pk__in=[product.pk for product in random_products]
                    ).order_by("-rating")
            else:
                return queryset.none()

    def filter_catalog_id_slider(self, queryset, name, value):
        pass
