from django.contrib import admin
from .models import *
from .AdminModels import OrderAdmin, AdditionalservicesAdmin, UtilsAdmin

admin.site.register(OrderFace, UtilsAdmin)
admin.site.register(OrderType, UtilsAdmin)
admin.site.register(PaymentType, UtilsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Additionalservices, AdditionalservicesAdmin)
