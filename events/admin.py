from django.contrib import admin

from .models import MuseumEvent


@admin.register(MuseumEvent)
class AdminMuseumEvent(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "date",
    )