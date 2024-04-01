from django.contrib import admin

from DB.models import ProductInfo


class ProductInfoInline(admin.TabularInline):
    model = ProductInfo
    extra = 0
