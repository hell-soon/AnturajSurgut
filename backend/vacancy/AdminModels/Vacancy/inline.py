from django.contrib import admin
from vacancy.models import ResponseVacancy


class InlineResponseVacancy(admin.StackedInline):
    model = ResponseVacancy
    extra = 0
    verbose_name = "Отклик"
    verbose_name_plural = "Отклики"
    readonly_fields = ("created_at",)
