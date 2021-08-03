# Generated by Django 3.2.3 on 2021-07-24 21:16

from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affaire', models.CharField(max_length=200)),
                ('incrimination', models.CharField(blank=True, max_length=200, null=True, verbose_name='Incrimination')),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, verbose_name='Nom Infraction')),
            ],
        ),
        migrations.CreateModel(
            name='Saisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroPv', models.IntegerField(blank=True, null=True)),
                ('objet', models.CharField(blank=True, max_length=300, null=True)),
                ('description', django_summernote.fields.SummernoteTextField(blank=True, null=True)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('vuEtTransmis', models.BooleanField(blank=True, default=False, null=True, verbose_name='Vu et Transmis')),
                ('ouvertureEnquete', models.BooleanField(blank=True, default=False, null=True, verbose_name='Ouverture Enquete')),
                ('crime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pojudiciaire.crime')),
            ],
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroPv', models.IntegerField(blank=True, null=True)),
                ('objet', models.CharField(blank=True, max_length=300, null=True)),
                ('description', django_summernote.fields.SummernoteTextField(blank=True, null=True)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('reference', models.CharField(blank=True, max_length=200, null=True)),
                ('crime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pojudiciaire.crime')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroPv', models.IntegerField(blank=True, null=True)),
                ('objet', models.CharField(blank=True, max_length=300, null=True)),
                ('description', django_summernote.fields.SummernoteTextField(blank=True, null=True)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('crime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pojudiciaire.crime')),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroPv', models.IntegerField(blank=True, null=True)),
                ('objet', models.CharField(blank=True, max_length=300, null=True)),
                ('description', django_summernote.fields.SummernoteTextField(blank=True, null=True)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('crime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pojudiciaire.crime')),
            ],
        ),
        migrations.CreateModel(
            name='Interrogatoire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroPv', models.IntegerField(blank=True, null=True)),
                ('objet', models.CharField(blank=True, max_length=300, null=True)),
                ('description', django_summernote.fields.SummernoteTextField(blank=True, null=True)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('crime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pojudiciaire.crime')),
            ],
        ),
        migrations.AddField(
            model_name='crime',
            name='typeInfraction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pojudiciaire.typeinfraction'),
        ),
        migrations.CreateModel(
            name='Confrontation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroPv', models.IntegerField(blank=True, null=True)),
                ('objet', models.CharField(blank=True, max_length=300, null=True)),
                ('description', django_summernote.fields.SummernoteTextField(blank=True, null=True)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('crime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pojudiciaire.crime')),
            ],
        ),
        migrations.CreateModel(
            name='Conduite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroPv', models.IntegerField(blank=True, null=True)),
                ('objet', models.CharField(blank=True, max_length=300, null=True)),
                ('description', django_summernote.fields.SummernoteTextField(blank=True, null=True)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('crime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pojudiciaire.crime')),
            ],
        ),
        migrations.CreateModel(
            name='Cloture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroPv', models.IntegerField(blank=True, null=True)),
                ('objet', models.CharField(blank=True, max_length=300, null=True)),
                ('description', django_summernote.fields.SummernoteTextField(blank=True, null=True)),
                ('dateCreation', models.DateTimeField(auto_now_add=True, null=True)),
                ('deroulementEtNotification', models.BooleanField(blank=True, default=False, null=True, verbose_name='Deroulement et Notification')),
                ('controleEtTransmission', models.BooleanField(blank=True, default=False, null=True, verbose_name='Controle et Transmission')),
                ('mentionRestitution', models.BooleanField(blank=True, default=False, null=True, verbose_name='Mention et Restition')),
                ('crime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pojudiciaire.crime')),
            ],
        ),
        migrations.CreateModel(
            name='Audition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroPv', models.IntegerField(blank=True, null=True)),
                ('objet', models.CharField(blank=True, max_length=300, null=True)),
                ('description', django_summernote.fields.SummernoteTextField(blank=True, null=True)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('crime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pojudiciaire.crime')),
            ],
        ),
    ]
