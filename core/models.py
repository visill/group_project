from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail


class BaseModelWithImage(models.Model):
    name = models.CharField(
        "название обьекта",
        max_length=100
    )
    slug = models.SlugField(
        "уникальный слаг(путь) для обьекта", max_length=100
    )
    description = models.TextField(
        "описание обьекта"
    )
    image = models.ImageField(
        "изображение обьекта", upload_to="uploads/%Y/%m"
    )

    class Meta:
        verbose_name = "модель с изображением"
        verbose_name_plural = "модели с изображением"
        abstract = True

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


class BaseEventModel(models.Model):
    title = models.CharField(
        "заголовок события", max_length=150
    )
    slug = models.SlugField(
        "уникальный слаг(путь) события", max_length=100
    )

    class Meta:
        verbose_name = "событие"
        verbose_name_plural = "события"
        abstract = True
