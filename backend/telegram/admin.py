from django.contrib import admin
from .models import TelegramNews, TelegramImage

# Register your models here.


class TelegramImageInline(admin.TabularInline):
    model = TelegramNews.image.through
    extra = 1


@admin.register(TelegramNews)
class TelegramNewsAdmin(admin.ModelAdmin):
    inlines = [TelegramImageInline]
    list_display = ["title", "description"]


admin.site.register(TelegramImage)
