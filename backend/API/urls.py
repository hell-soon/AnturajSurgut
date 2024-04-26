from django.urls import path, include

from .Views.Search import GlobalSearch
from .Views.Filters import FilterMenu
from .Routers.routers import router


urlpatterns = [
    path("", include(router.urls)),
    path("search/", GlobalSearch.as_view()),
    path("filters/", FilterMenu.as_view()),
]
