from django.contrib import admin
from django.db import models

from image_uploader_widget.widgets import ImageUploaderWidget

from sitedb.models import SocialAccount, WokrTime, Address, Contact, Requisites


class SocialInline(admin.TabularInline):
    model = SocialAccount
    extra = 1

    class Media:
        css = {
            "all": ("css/ImageUploader.css",),
        }

    formfield_overrides = {
        models.ImageField: {"widget": ImageUploaderWidget},
    }


class WorkTimeInline(admin.TabularInline):
    model = WokrTime
    extra = 1
    max_num = 1


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1
    max_num = 1


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1
    max_num = 1


class RequisitesInline(admin.TabularInline):
    model = Requisites
    extra = 1
    max_num = 1
