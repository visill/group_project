from django.contrib import admin

from events.models import MuseumEvent
from exhibits.models import Exhibit
from museums.models import City, Museum


@admin.register(Exhibit)
class AdminExhibit(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "museum",
        "image_tmb",
    )


@admin.register(Museum)
class AdminMuseum(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "image_tmb",
    )


@admin.register(City)
class AdminCity(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )


@admin.register(MuseumEvent)
class AdminMuseumEvent(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "date",
    )
