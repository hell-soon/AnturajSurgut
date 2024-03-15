from django.contrib import admin
from DB.models import SubCatalog


class SubCatalogAdmin(admin.TabularInline):
    model = SubCatalog
    extra = 0  # fields to show in admin
