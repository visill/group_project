from django.db import models

from core.models import BaseModelWithImage


class City(models.Model):
    name = models.CharField(max_length=168)
    slug = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Museum(BaseModelWithImage):
    address = models.TextField(blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    link = models.TextField(default='У данного музея нет собственного сайта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Музей'
        verbose_name_plural = 'Музеи'
