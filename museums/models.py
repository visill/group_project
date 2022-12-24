from django.db import models

from core.models import BaseModelWithImage


class City(models.Model):
    name = models.CharField(max_length=168)
    slug = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"


class Museum(BaseModelWithImage):
    address = models.TextField(blank=True)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="museums"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "музей"
        verbose_name_plural = "музеи"
