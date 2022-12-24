from django.db import models

from core.models import BaseModelWithImage


class CityManager(models.Manager):
    def get_city_by_slug(slug):
        return City.objects.get(slug=slug)


class City(models.Model):
    name = models.CharField("название города", max_length=168)
    slug = models.CharField("уникальный слаг(путь) города", max_length=150)

    objects = CityManager()

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"

    def __str__(self):
        return self.name


class Museum(BaseModelWithImage):
    address = models.TextField("адрес музея", blank=True)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="museums",
        verbose_name="город, в котором расположен текущий музей",
    )

    class Meta:
        verbose_name = "музей"
        verbose_name_plural = "музеи"

    def __str__(self):
        return self.name
