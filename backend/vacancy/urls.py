from django.urls import path, include

from .views import VacancyView


urlpatterns = [
    path("test/", VacancyView.as_view()),
]
