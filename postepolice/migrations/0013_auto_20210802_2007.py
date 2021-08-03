# Generated by Django 3.2.3 on 2021-08-02 20:07

from django.db import migrations, models
import django.utils.timezone
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('postepolice', '0012_auto_20210802_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='gardeavue',
            name='aupres_de',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Auprès de'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='date_conduite',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date conduite'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='date_debut',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date de debut'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='date_naissance',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date de naissance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='date_prolongation',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date de la prolongation de la garde à vue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='date_pv',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date PV'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='decision_magistrat',
            field=models.CharField(choices=[('AC', 'Accorée'), ('RE', 'Refusé')], default='AC', max_length=255, verbose_name='Décision du magistrat'),
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='devant',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Devant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='domicile',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Domicile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='duree_audition',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Durée audition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='duree_repos',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Durée repos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='heure_conduite',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Heure conduite'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='heure_debut',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Heure'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='heure_debut_audition',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Heure de debut audition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='heure_debut_repos',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Heure de debut repos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='heure_fin_audition',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='heure de fin audition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='heure_fin_repos',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='heure de fin repos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='heure_prolongation',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Heure de la prolongation de la garde à vue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='liberte',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Liberté'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='lieu_naissance',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Lieu de naissance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='motif',
            field=django_summernote.fields.SummernoteTextField(default=django.utils.timezone.now, verbose_name='Motif de la garde à vue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='nom',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Nom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='numero_pv',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='P.V.n°'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='observations',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Observations'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='prenom',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Prénom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='prise_par',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Prise par'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gardeavue',
            name='profession',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Profession'),
            preserve_default=False,
        ),
    ]
