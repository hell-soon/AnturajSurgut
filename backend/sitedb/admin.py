from django.contrib import admin

from sitedb.models import *
from .AdminModels import (
    SertificateAdmin,
    SiteImageAdmin,
    OurWorkAdmin,
    ServiceAdmin,
    SliderAdmin,
    ContactAdmin,
    SocailAdmin,
    RequisitesAdmin,
    AddressAdmin,
    WokrTimeAdmin,
)

admin.site.register(OurWorkImage, SiteImageAdmin)
admin.site.register(SiteImage, SiteImageAdmin)
admin.site.register(SocialAccount, SocailAdmin)
admin.site.register(Sertificate, SertificateAdmin)
admin.site.register(OurWork, OurWorkAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Slider, SliderAdmin)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Requisites, RequisitesAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(WokrTime, WokrTimeAdmin)
