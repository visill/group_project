# Generated by Django 3.2.16 on 2022-12-24 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibits', '0002_auto_20221224_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='image',
            field=models.ImageField(upload_to='uploads/%Y/%m', verbose_name='изображение обьекта'),
        ),
    ]
