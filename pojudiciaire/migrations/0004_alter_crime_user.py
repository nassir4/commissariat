# Generated by Django 3.2.3 on 2021-08-04 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pojudiciaire', '0003_crime_etat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='user',
            field=models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'police judiciaire'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Agent'),
        ),
    ]
