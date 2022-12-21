# Generated by Django 3.2.16 on 2022-12-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museums', '0005_alter_museum_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=168)),
                ('slug', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
    ]
