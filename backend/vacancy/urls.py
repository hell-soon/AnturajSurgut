from django.urls import path, include

from .views import VacancyView


urlpatterns = [
    path("test/", VacancyView.as_view()),
    path("test/<int:id>/", VacancyView.as_view()),
]
