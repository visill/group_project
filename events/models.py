from django.db import models

from core.models import BaseEventModel
from museums.models import Museum


class MuseumEvent(BaseEventModel):
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
