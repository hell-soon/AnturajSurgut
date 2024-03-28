from django.contrib import admin
from .models import *
from .AdminModels import OrderAdmin, AdditionalservicesAdmin

admin.site.register(Order, OrderAdmin)
admin.site.register(Additionalservices, AdditionalservicesAdmin)
