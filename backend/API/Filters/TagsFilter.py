from django_filters import filters, ModelMultipleChoiceFilter
from django_filters.rest_framework import FilterSet

from django.db.models import Q, Count

from DB.models import Product, Tags, SubCatalog


class TagsFilter(FilterSet):
    catalog_id = filters.NumberFilter(method="filter_catalog_id", label="По каталогу")
    subcatalog_id = ModelMultipleChoiceFilter(
        queryset=SubCatalog.objects.all(),
        method="filter_sub_catalog_id",
        label="По подкаталогу",
        required=False,
    )

    class Meta:
        model = Tags
        fields = ["catalog_id", "subcatalog_id"]

    def filter_catalog_id(self, queryset, name, value):
        sub_catalogs = SubCatalog.objects.filter(catalog__id=value)
        products = Product.objects.filter(
            Q(sub_catalog__in=sub_catalogs) & Q(product_status=True)
        )
        unique_tags = (
            Tags.objects.filter(product__in=products)
            .annotate(product_count=Count("product"))
            .distinct()
            .order_by("id")
        )

        return unique_tags

    def filter_sub_catalog_id(self, queryset, name, value):
        if not value:
            return queryset
        products = Product.objects.filter(sub_catalog__in=value)
        unique_tags = (
            Tags.objects.filter(product__in=products)
            .annotate(product_count=Count("product"))
            .distinct()
            .order_by("id")
        )
        return unique_tags
