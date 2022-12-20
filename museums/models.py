from core.models import BaseModelWithImage
from django.db import models


class Museum(BaseModelWithImage):
    address = models.TextField(blank=True)
    city = models.CharField(max_length=168, blank=True)
    link = models.TextField(default='У данного музея нет собственного сайта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Музей'
        verbose_name_plural = 'Музеи'
