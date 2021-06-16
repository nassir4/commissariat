# Generated by Django 3.2.3 on 2021-06-16 02:20

from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accident', '0010_auto_20210607_0631'),
    ]

    operations = [
        migrations.CreateModel(
            name='PV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroPv', models.IntegerField()),
                ('objet', models.CharField(max_length=300)),
                ('description', django_summernote.fields.SummernoteTextField(blank=True, null=True)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Audition',
            fields=[
                ('pv_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accident.pv')),
                ('affaire', models.CharField(max_length=200)),
                ('incrimination', models.CharField(max_length=100)),
            ],
            bases=('accident.pv',),
        ),
        migrations.CreateModel(
            name='Cloture',
            fields=[
                ('pv_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accident.pv')),
                ('affaire', models.CharField(max_length=200)),
                ('incrimination', models.CharField(max_length=100)),
                ('deroulementEtNotification', models.BooleanField(verbose_name=True)),
                ('controleEtTransmission', models.BooleanField(verbose_name=True)),
                ('mentionRestitution', models.BooleanField(verbose_name=True)),
            ],
            bases=('accident.pv',),
        ),
        migrations.CreateModel(
            name='Conduite',
            fields=[
                ('pv_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accident.pv')),
                ('affaire', models.CharField(max_length=200)),
                ('incrimination', models.CharField(max_length=100)),
            ],
            bases=('accident.pv',),
        ),
        migrations.CreateModel(
            name='Confrontation',
            fields=[
                ('pv_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accident.pv')),
                ('affaire', models.CharField(max_length=200)),
                ('incrimination', models.CharField(max_length=100)),
            ],
            bases=('accident.pv',),
        ),
        migrations.CreateModel(
            name='Interrogatoire',
            fields=[
                ('pv_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accident.pv')),
                ('affaire', models.CharField(max_length=200)),
                ('incrimination', models.CharField(max_length=100)),
            ],
            bases=('accident.pv',),
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('pv_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accident.pv')),
                ('affaire', models.CharField(max_length=200)),
                ('incrimination', models.CharField(max_length=100)),
            ],
            bases=('accident.pv',),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('pv_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accident.pv')),
                ('affaire', models.CharField(max_length=200)),
                ('incrimination', models.CharField(max_length=100)),
            ],
            bases=('accident.pv',),
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('pv_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accident.pv')),
                ('reference', models.CharField(max_length=200)),
            ],
            bases=('accident.pv',),
        ),
        migrations.CreateModel(
            name='Saisine',
            fields=[
                ('pv_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accident.pv')),
                ('affaire', models.CharField(max_length=200)),
                ('incrimination', models.CharField(max_length=100)),
                ('vuEtTransmis', models.BooleanField(default=True, verbose_name='Vu et Transmis')),
                ('ouvertureEnquete', models.BooleanField(default=True, verbose_name='Ouverture Enquete')),
            ],
            bases=('accident.pv',),
        ),
    ]
