from django.db import models

from core.models import BaseEventModel
from museums.models import Museum


class MuseumEventManager(models.Manager):
    def get_event_by_city(city_slug):
        events = MuseumEvent.objects.filter(
            museum__city__slug=city_slug
        ).order_by("-date")
        return events


class MuseumEvent(BaseEventModel):
    museum = models.ForeignKey(
        Museum,
        on_delete=models.CASCADE,
        related_name="events",
        verbose_name="музей, в котором происходит это событие",
    )
    date = models.DateField("дата события")
    description = models.TextField("описание события")

    objects = MuseumEventManager()

    class Meta:
        verbose_name = "событие"
        verbose_name_plural = "события"

    def __str__(self):
        return self.title
