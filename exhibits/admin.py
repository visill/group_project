from django.contrib import admin

from .models import Exhibit


@admin.register(Exhibit)
class AdminExhibit(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "museum",
        "image_tmb",
    )