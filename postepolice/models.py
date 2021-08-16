from random import choices

from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import ForeignKey
from django_summernote.fields import SummernoteTextField

from accident.views import modifierDeclaration

ROLES = (
    ('Chef de poste', '0'),
    ('Secretaire', '1'),
    ('Chauffeur', '2'),
    ('Police de secours', '3')
)


# modele agent poste
class AgentPoste(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField("Role", max_length=100, choices=ROLES)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'



# modele brigade
class Brigade(models.Model):
    nom = models.CharField("Nom", max_length=200, unique=True)
    chef_de_poste = models.OneToOneField(AgentPoste, on_delete=models.SET_NULL,
                                         null=True, blank=True, related_name="is_chef_de_poste")
    secretaire = models.ManyToManyField(AgentPoste,
                                      null=True, blank=True, related_name="is_secretaire")
    chauffeur = models.ManyToManyField(AgentPoste,
                                     null=True, blank=True, related_name="is_chauffeur")

    def __str__(self):
        return self.nom

class Registre(models.Model):
    nom = models.CharField("Nom",max_length=200,null=True,blank=True)
    brigade = models.ForeignKey(Brigade, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField("Date", auto_now_add=True)
    status = models.BooleanField("Status", default=False)

    def __str__(self):
        return self.nom

class MainCourante(models.Model):
    registre = models.ForeignKey(Registre, on_delete=models.CASCADE,blank=True,null=True)
    numero_mention = models.IntegerField("Numero mention", null=True, blank=True)
    heure = models.TimeField("Heure", auto_now_add=False)
    motif = SummernoteTextField("Motif")
    vue = models.CharField("Vue",null=True, blank=True, max_length=255)
    affecte = models.ForeignKey(User, on_delete=models.SET_NULL,
                                blank=True, null=True, verbose_name='Affectée à',
                                limit_choices_to={'groups__name': 'police judiciaire'},)
    def __str__(self):
        return self.numero_mention


class Plainte(models.Model):
    registre = models.ForeignKey(Registre, on_delete=models.CASCADE, blank=True, null=True)
    numero_mention = models.IntegerField("Numero mention", null=True, blank=True)
    heure = models.TimeField("Heure", auto_now_add=False)
    motif = SummernoteTextField("Contenu")
    photo1 = models.ImageField(upload_to='images/')
    photo2= models.ImageField(upload_to='images/')
    affecte= models.ForeignKey(User, on_delete=models.SET_NULL,
                             blank=True, null=True, verbose_name='Affectée à',
                             limit_choices_to={'groups__name': 'police judiciaire'}, )
    # signature
    status = models.BooleanField("Status", default=False)

    def __str__(self):
        return f'{self.numero_mention}'


class Perte(models.Model):
    registre = models.ForeignKey(Registre, on_delete=models.CASCADE,blank=True,null=True)
    numero_mention = models.IntegerField("Numero mention", null=True, blank=True)
    heure = models.TimeField("Heure", auto_now_add=False)
    motif = SummernoteTextField("Contenu")
    status = models.BooleanField("Status", default=False)

    def __str__(self):
        return self.numero_mention


class ObjectConsigne(models.Model):
    nom = models.CharField("Nom", max_length=200)
    description = models.TextField("Description", blank=True, null=True)

    def __str__(self):
        return self.nom


class Ecrou(models.Model):
    registre = models.ForeignKey(Registre, on_delete=models.CASCADE,blank=True,null=True)
    numero_mention = models.IntegerField("Numero mention", null=True, blank=True)
    heure = models.TimeField("Heure", auto_now_add=False)
    petite_identite = SummernoteTextField("Petite identité")
    objects_consignes = models.CharField("Objet consigné",max_length=400, blank=True,null=True)
    motif_garde_vue = models.CharField("Motif garde à vue",max_length=255)
    suite = models.CharField("Suite",max_length=255)
    status = models.BooleanField("Status", default=False)

    def __str__(self):
        return self.numero_mention

class GardeAVue(models.Model):
    numero = models.IntegerField("N°", null=True, blank=True)
    registre = models.ForeignKey(Registre, on_delete=models.CASCADE,blank=True,null=True)
    nom = models.CharField("Nom", max_length=255,blank=True,null=True)
    prenom = models.CharField("Prénom",max_length=255,blank=True,null=True)
    date_naissance = models.DateField("Date de naissance", auto_now=False,blank=True,null=True)
    lieu_naissance = models.CharField("Lieu de naissance", max_length=255,blank=True,null=True)
    profession = models.CharField("Profession", max_length=255,blank=True,null=True)
    domicile = models.CharField("Domicile",max_length=255,blank=True,null=True)
    motif = models.TextField("Motif de la garde à vue",blank=True,null=True)
    prise_par = models.CharField("Prise par", max_length=255,blank=True,null=True)
    date_debut = models.DateField("Date de debut",auto_now=False,blank=True,null=True)
    heure_debut = models.TimeField("Heure",auto_now=False,blank=True,null=True)
    heure_debut_audition = models.TimeField("Heure de debut audition",auto_now=False,blank=True,null=True)
    heure_fin_audition = models.TimeField("heure de fin audition", auto_now=False,blank=True,null=True)
    duree_audition = models.CharField("Durée audition",max_length=255,blank=True,null=True)
    heure_debut_repos = models.TimeField("Heure de debut repos", auto_now=False,blank=True,null=True)
    heure_fin_repos = models.TimeField("heure de fin repos", auto_now=False,blank=True,null=True)
    duree_repos = models.CharField("Durée repos", max_length=255,blank=True,null=True)
    liberte = models.CharField("Liberté", max_length=255,blank=True,null=True)
    date_conduite = models.DateField("Date conduite", auto_now=False,blank=True,null=True)
    heure_conduite = models.TimeField("Heure conduite", auto_now=False,blank=True,null=True)
    devant = models.CharField("Devant", max_length=255,blank=True,null=True)
    numero_pv = models.CharField("P.V.n°", max_length=255,blank=True,null=True)
    date_pv = models.DateField("Date PV", auto_now=False,blank=True,null=True)
    date_prolongation = models.DateField("Date de la prolongation de la garde à vue", auto_now=False,blank=True,null=True)
    heure_prolongation = models.TimeField("Heure de la prolongation de la garde à vue", auto_now=False,blank=True,null=True)
    aupres_de = models.CharField("Auprès de", max_length=255,blank=True,null=True)
    Decision_choice=(
        ('AC','Accorée'),
        ('RE','Refusé')
    )
    decision_magistrat = models.CharField("Décision du magistrat", default='AC', choices=Decision_choice, max_length=255,blank=True,null=True)
    observations = models.CharField("Observations", max_length=255,blank=True,null=True)

class PoliceSecours(models.Model):
    prenom = models.CharField("Prénom", max_length=255,blank=True,null=True)
    nom = models.CharField("Nom", max_length=255, blank=True,null=True)
    registre = ForeignKey(Registre, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.prenom} {self.nom}'