from django.contrib import admin
from .models import TelegramNews, TelegramImage, TelegramImageOrder

# Register your models here.


@admin.register(TelegramImageOrder)
class TelegramImageOrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_status",
        "image",
    )


class TelegramImageInline(admin.TabularInline):
    model = TelegramNews.image.through
    extra = 1


@admin.register(TelegramNews)
class TelegramNewsAdmin(admin.ModelAdmin):
    inlines = [TelegramImageInline]
    list_display = ["title", "description"]


admin.site.register(TelegramImage)
