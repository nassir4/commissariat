# Generated by Django 3.2.3 on 2021-06-07 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accident', '0009_auto_20210607_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assurance',
            name='vehicule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.vehicule'),
        ),
        migrations.AlterField(
            model_name='avertisseur',
            name='vehicule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.vehicule'),
        ),
        migrations.AlterField(
            model_name='conducteur',
            name='vehicule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.vehicule'),
        ),
        migrations.AlterField(
            model_name='declaration',
            name='conducteur',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.conducteur'),
        ),
        migrations.AlterField(
            model_name='eclairage',
            name='vehicule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.vehicule'),
        ),
        migrations.AlterField(
            model_name='essuieglace',
            name='vehicule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.vehicule'),
        ),
        migrations.AlterField(
            model_name='etatdeslieux',
            name='accident',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.accident'),
        ),
        migrations.AlterField(
            model_name='indicateurdirection',
            name='vehicule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.vehicule'),
        ),
        migrations.AlterField(
            model_name='indicateurvitesse',
            name='vehicule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.vehicule'),
        ),
        migrations.AlterField(
            model_name='permis',
            name='conducteur',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.conducteur'),
        ),
        migrations.AlterField(
            model_name='proprietaire',
            name='vehicule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.vehicule'),
        ),
        migrations.AlterField(
            model_name='retroviseur',
            name='vehicule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.vehicule'),
        ),
        migrations.AlterField(
            model_name='temoin',
            name='accident',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.accident'),
        ),
        migrations.AlterField(
            model_name='victime',
            name='accident',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.accident'),
        ),
        migrations.AlterField(
            model_name='vignette',
            name='vehicule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accident.vehicule'),
        ),
    ]
