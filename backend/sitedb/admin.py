from django.contrib import admin

from sitedb.models import *
from .AdminModels import (
    SertificateAdmin,
    OurWorkImageAdmin,
    NewsAdmin,
    OurWorkAdmin,
    ServiceAdmin,
    SliderAdmin,
    ContactAdmin,
    SocailAdmin,
)


admin.site.register(SocialAccount, SocailAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Sertificate, SertificateAdmin)
admin.site.register(OurWorkImage, OurWorkImageAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(OurWork, OurWorkAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Slider, SliderAdmin)
