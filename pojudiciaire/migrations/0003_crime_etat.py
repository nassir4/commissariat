# Generated by Django 3.2.3 on 2021-08-04 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pojudiciaire', '0002_crime_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='crime',
            name='etat',
            field=models.CharField(choices=[('EC', 'En cours'), ('TE', 'Terminée')], default='EC', max_length=255, verbose_name='Etat'),
        ),
    ]
