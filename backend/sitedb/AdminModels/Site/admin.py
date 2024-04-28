from django.contrib import admin
from .inline import *


class SiteInfoAdmin(admin.ModelAdmin):
    inlines = [ContactInline, AddressInline, WorkTimeInline, SocialInline]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
