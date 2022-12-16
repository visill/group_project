from django.contrib import admin

from exhibits.models import Exhibit
from museums.models import Museum


@admin.register(Exhibit)
class AdminExhibit(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'museum',
        'image_tmb',
        )


@admin.register(Museum)
class AdminMuseum(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'image_tmb',
        )
