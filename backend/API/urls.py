from django.urls import path, include
from .Views.Product import ProductViewSet
from .Views.Search import GlobalSearch
from .Views.Filters import FilterMenu
from .Routers.routers import router


urlpatterns = [
    path("", include(router.urls)),
    path("list/", ProductViewSet.as_view({"get": "list"})),
    path("list/<int:pk>/", ProductViewSet.as_view({"get": "info"})),
    path("search/", GlobalSearch.as_view()),
    path("filters/", FilterMenu.as_view()),
]
