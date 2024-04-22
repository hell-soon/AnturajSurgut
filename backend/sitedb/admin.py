from django.contrib import admin

from sitedb.models import *
from .AdminModels import (
    SertificateAdmin,
    SiteImageAdmin,
    OurWorkAdmin,
    ServiceAdmin,
    SliderAdmin,
    SiteInfoAdmin,
)


admin.site.register(SiteInfo, SiteInfoAdmin)
admin.site.register(OurWorkImage, SiteImageAdmin)
admin.site.register(SiteImage, SiteImageAdmin)
admin.site.register(Sertificate, SertificateAdmin)
admin.site.register(OurWork, OurWorkAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Slider, SliderAdmin)
