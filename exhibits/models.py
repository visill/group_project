from django.db import models

from core.models import BaseModelWithImage
from museums.models import Museum


class Exhibit(BaseModelWithImage):
    museum = models.ForeignKey(
        Museum, on_delete=models.CASCADE, related_name="exhibits"
    )

    class Meta:
        verbose_name = "экспонат"
        verbose_name_plural = "экспонаты"

    def __str__(self):
        return self.name
