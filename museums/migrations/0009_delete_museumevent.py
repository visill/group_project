# Generated by Django 3.2.16 on 2022-12-22 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("museums", "0008_museumevent"),
    ]

    operations = [
        migrations.DeleteModel(
            name="MuseumEvent",
        ),
    ]