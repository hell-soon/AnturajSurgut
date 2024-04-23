from django.contrib import admin
from .models import Vacancy
from .AdminModels.Vacancy.admin import VacancyAdmin


admin.site.register(Vacancy, VacancyAdmin)
