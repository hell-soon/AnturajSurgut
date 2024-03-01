from django_filters import rest_framework as filters
from DB.models import Catalog, SubCatalog


class CatalogFilter(filters.FilterSet):
    catalog_id = filters.NumberFilter(field_name="catalog__id")

    class Meta:
        model = Catalog
        fields = ["catalog_id"]


class SubCatalogFilter(filters.FilterSet):
    catalog_id = filters.NumberFilter(field_name="catalog__id")

    class Meta:
        model = SubCatalog
        fields = ["catalog_id"]
