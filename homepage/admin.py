from django.contrib import admin

from .models import HPEvent


@admin.register(HPEvent)
class AdminCity(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        )