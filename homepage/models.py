from core.models import BaseEventModel
from django.db import models
from museums.models import City


class HPEvent(BaseEventModel):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
