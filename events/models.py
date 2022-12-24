from django.db import models

from core.models import BaseEventModel
from museums.models import Museum


class MuseumEvent(BaseEventModel):
    museum = models.ForeignKey(
        Museum, on_delete=models.CASCADE, related_name="events",
        verbose_name="музей, в котором происходит это событие"
    )
    date = models.DateField("дата события")
    description = models.TextField("описание события")

    class Meta:
        verbose_name = "событие"
        verbose_name_plural = "события"

    def __str__(self):
        return self.title
