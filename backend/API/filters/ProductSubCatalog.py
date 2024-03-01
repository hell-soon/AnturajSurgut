from django_filters import rest_framework as filters
from DB.models import Product


# Фильтр для товара через id подкаталога
class ProductFilter(filters.FilterSet):
    catalog_id = filters.NumberFilter(field_name="catalog__id")

    class Meta:
        model = Product
        fields = ["catalog_id"]
