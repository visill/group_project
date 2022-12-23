from django.db import models

from core.models import BaseModelWithImage
from museums.models import Museum


class Exhibit(BaseModelWithImage):
    museum = models.ForeignKey(
        Museum, on_delete=models.CASCADE, related_name="exhibits"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Экспонат"
        verbose_name_plural = "Экспонаты"
