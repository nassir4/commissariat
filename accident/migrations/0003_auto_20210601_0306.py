# Generated by Django 3.2.3 on 2021-06-01 03:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accident', '0002_auto_20210601_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident',
            name='date_accident',
            field=models.DateField(default=datetime.datetime(2021, 6, 1, 3, 5, 46, 248369, tzinfo=utc), verbose_name='Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accident',
            name='heure_accident',
            field=models.TimeField(default=datetime.datetime(2021, 6, 1, 3, 6, 9, 760135, tzinfo=utc), verbose_name='Heure'),
            preserve_default=False,
        ),
    ]
