from django.contrib import admin

from sitedb.models import Slider, Service, News, OurWorkImage, OurWork, Sertificate
from .AdminModels import SertificateAdmin

# Register your models here.


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "url", "created_at")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "url", "created_at")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "created_at", "image")


@admin.register(OurWorkImage)
class OurWorkImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


@admin.register(OurWork)
class OurWorkAdmin(admin.ModelAdmin):
    list_display = ("title", "work_list", "description")


admin.site.register(Sertificate, SertificateAdmin)
