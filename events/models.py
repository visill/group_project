from django.db import models

from core.models import BaseEventModel
from museums.models import Museum


class MuseumEvent(BaseEventModel):
    museum = models.ForeignKey(
        Museum, on_delete=models.CASCADE, related_name="events"
    )
    date = models.DateField()
    description = models.TextField()

    class Meta:
        verbose_name = "событие"
        verbose_name_plural = "события"

    def __str__(self):
        return self.title
