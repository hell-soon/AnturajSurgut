from django.contrib import admin
from .inline import *


class SiteInfoAdmin(admin.ModelAdmin):
    inlines = [ContactInline, AddressInline, WorkTimeInline, SocialInline]
