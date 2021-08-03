# Generated by Django 3.2.3 on 2021-08-01 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postepolice', '0007_auto_20210801_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perte',
            old_name='contenu',
            new_name='motif',
        ),
        migrations.RenameField(
            model_name='plainte',
            old_name='objet',
            new_name='motif',
        ),
        migrations.RemoveField(
            model_name='perte',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='perte',
            name='code_postal',
        ),
        migrations.RemoveField(
            model_name='perte',
            name='nom_prenom',
        ),
        migrations.RemoveField(
            model_name='perte',
            name='objet',
        ),
        migrations.RemoveField(
            model_name='perte',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='perte',
            name='ville',
        ),
        migrations.RemoveField(
            model_name='plainte',
            name='nom_prenom',
        ),
    ]
