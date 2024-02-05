from django.contrib import admin

from .models import CustomUser


# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('phone_number', 'first_name', 'last_name',  'email', 'is_staff')


admin.site.register(CustomUser)