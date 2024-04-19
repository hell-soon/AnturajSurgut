from django.contrib import admin


class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "fax")


class RequisitesAdmin(admin.ModelAdmin):
    list_display = ("ip", "inn", "legal_address")


class AddressAdmin(admin.ModelAdmin):
    list_display = ("address", "longitude", "latitude")


class WokrTimeAdmin(admin.ModelAdmin):
    list_display = ("work_time",)

