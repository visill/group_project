from django.contrib import admin

from museums.models import City, Museum


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
