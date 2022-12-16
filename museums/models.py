from django.db import models

from core.models import WithImage


class Museum(models.Model, WithImage):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    description = models.TextField()


class Exhibit(models.Model, WithImage):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)

    description = models.TextField()
