from django.contrib import admin
from .inline import InlineResponseVacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "created_at",
        "updated_at",
        "work_place",
    )
    inlines = [InlineResponseVacancy]
