# Generated by Django 3.2.3 on 2021-06-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accident', '0007_auto_20210606_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conducteur',
            name='date_naissance',
            field=models.DateField(blank=True, null=True, verbose_name='Date de naissance'),
        ),
    ]
