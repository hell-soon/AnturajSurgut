from django.contrib import admin

from DB.models import ProductInfo


class ProductInfoInline(admin.StackedInline):
    model = ProductInfo
    extra = 0
