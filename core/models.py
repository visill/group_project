from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail


class BaseModelWithImage(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="uploads/%Y/%m")

    @property
    def get_img(self):
        return get_thumbnail(self.image, "300x300", crop="center", quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(f'<img src="{self.get_img.url}"')
        return "Нет изображения"

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs["file"])

    cleanup_pre_delete.connect(sorl_delete)

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"
        abstract = True


class BaseEventModel(models.Model):
    title = models.CharField(max_length=150)
    link = models.TextField(blank=True)

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
        abstract = True
