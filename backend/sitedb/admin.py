from django.contrib import admin

from sitedb.models import Slider, Service, Review, News, OurWorkImage, OurWork


# Register your models here.

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'url', 'created_at')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'url', 'created_at')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'rating', 'user', 'created_at')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_at', 'image')


@admin.register(OurWorkImage)
class OurWorkImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(OurWork)
class OurWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'work_list', 'description')
