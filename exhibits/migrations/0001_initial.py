# Generated by Django 3.2.16 on 2022-12-16 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('museums', '0002_delete_exhibit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/%Y/%m')),
                ('museum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibits', to='museums.museum')),
            ],
            options={
                'verbose_name': 'Экспонат',
                'verbose_name_plural': 'Экспонаты',
            },
        ),
    ]