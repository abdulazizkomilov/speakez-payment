from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "total", "is_finished", "created_at")
    list_filter = ("is_finished", "created_at")
    search_fields = ("id", "user_id")
    ordering = ("-created_at",)
