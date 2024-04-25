from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    date_hierarchy = "date_joined"
    empty_value_display = "-"
    search_fields = ("first_name", "last_name", "phone", "email")
    list_filter = ("is_staff",)
    list_display_links = ("id", "first_name", "last_name")
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone",
        "email",
        "date_joined",
        "is_staff",
    )
    fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "password",
        "is_staff",
        "is_superuser",
        "groups",
        "user_permissions",
        "username",
        "tg_id",
    )

    filter_horizontal = ("groups", "user_permissions")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Удалите поля, которые вы не хотите видеть при создании пользователя
        if not obj:
            form.base_fields.pop("date_joined", None)
            form.base_fields.pop("last_login", None)
            form.base_fields.pop("is_active", None)
        return form
