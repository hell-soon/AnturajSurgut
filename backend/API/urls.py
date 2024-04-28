from django.urls import path, include
from .Views.Catalogs import CatalogViewSet
from .Views.Tags import TagsViewSet
from .Views.SubCatalogs import SubCatalogViewSet
from .Views.Product import ProductViewSet
from .Views.Search import GlobalSearch
from .Views.Filters import FilterMenu


urlpatterns = [
    path("catalog/", CatalogViewSet.as_view({"get": "list"})),
    path("subcatalog/", SubCatalogViewSet.as_view({"get": "list"})),
    path("tags/", TagsViewSet.as_view({"get": "list"})),
    path("list/", ProductViewSet.as_view({"get": "list"})),
    path("list/<int:pk>/", ProductViewSet.as_view({"get": "info"})),
    path("search/", GlobalSearch.as_view()),
    path("filters/", FilterMenu.as_view()),
]
