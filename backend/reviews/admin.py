from django.contrib import admin
from .models import Review, Feedback

from .AdminModels.Feedback.admin import FeedbackAdmin


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "text",
        "rating",
        "created_at",
    )


admin.site.register(Feedback, FeedbackAdmin)
