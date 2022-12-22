# Generated by Django 3.2.16 on 2022-12-22 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('museums', '0009_delete_museumevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='MuseumEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('museum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='museums.museum')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
                'abstract': False,
            },
        ),
    ]
