from django.contrib import admin
from sitedb.models import ServiceOurWork, ServiceSlider


class ServiceOurWorkInline(admin.TabularInline):
    model = ServiceOurWork
    verbose_name = "Наша работа"
    verbose_name_plural = "Наши работы"
    extra = 0


class ServiceSliderInline(admin.TabularInline):
    model = ServiceSlider
    verbose_name = "Слайдер"
    verbose_name_plural = "Слайдеры"
    extra = 3
