from django.contrib import admin
from .models import News, Feedback

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "created_at")
    search_fields = ("first_name", "last_name", "email", "message")
    list_filter = ("created_at",)
