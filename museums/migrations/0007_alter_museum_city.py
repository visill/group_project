# Generated by Django 3.2.16 on 2022-12-20 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('museums', '0006_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museum',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='museums.city'),
        ),
    ]
