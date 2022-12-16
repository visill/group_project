from core.models import BaseModelWithImage


class Museum(BaseModelWithImage):
    class Meta:
        verbose_name = 'Музей'
        verbose_name_plural = 'Музеи'
