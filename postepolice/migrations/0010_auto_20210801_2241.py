# Generated by Django 3.2.3 on 2021-08-01 22:41

from django.db import migrations
import django.utils.timezone
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('postepolice', '0009_alter_maincourante_motif'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecrou',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='ecrou',
            name='code_postal',
        ),
        migrations.RemoveField(
            model_name='ecrou',
            name='nom_prenom',
        ),
        migrations.RemoveField(
            model_name='ecrou',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='ecrou',
            name='ville',
        ),
        migrations.AddField(
            model_name='ecrou',
            name='petite_identite',
            field=django_summernote.fields.SummernoteTextField(default=django.utils.timezone.now, verbose_name='Petite identité'),
            preserve_default=False,
        ),
    ]
