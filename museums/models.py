from django.db import models

from core.models import BaseModelWithImage


class City(models.Model):
    name = models.CharField(max_length=168)
    slug = models.CharField(max_length=150)

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"

    def __str__(self):
        return self.name


class Museum(BaseModelWithImage):
    address = models.TextField(blank=True)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="museums"
    )

    class Meta:
        verbose_name = "музей"
        verbose_name_plural = "музеи"

    def __str__(self):
        return self.name
