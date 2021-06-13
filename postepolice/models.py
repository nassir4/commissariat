from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django_summernote.fields import SummernoteTextField

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
        return self.user


# modele brigade
class Brigade(models.Model):
    nom = models.CharField("Nom", max_length=200, unique=True)
    chef_de_poste = models.OneToOneField(AgentPoste, on_delete=models.SET_NULL,
                                         null=True, blank=True, related_name="is_chef_de_poste")
    secretaire = models.OneToOneField(AgentPoste, on_delete=models.SET_NULL,
                                      null=True, blank=True, related_name="is_secretaire")
    chauffeur = models.OneToOneField(AgentPoste, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name="is_chauffeur")
    police_secours = models.ManyToManyField(AgentPoste)

    def __str__(self):
        return self.nom


class MainCourante(models.Model):
    brigade = models.ForeignKey(Brigade, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField("Date", auto_now_add=True)
    numero_mention = models.IntegerField("Numero mention", null=True, blank=True)
    heure = models.TimeField("Heure", auto_now_add=False)
    motif = models.TextField("Motif")

    def __str__(self):
        return self.numero_mention


class Plainte(models.Model):
    brigade = models.ForeignKey(Brigade, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField("Date", auto_now_add=True)
    numero_mention = models.IntegerField("Numero mention", null=True, blank=True)
    heure = models.TimeField("Heure", auto_now_add=False)
    nom_prenom = models.CharField("Nom et Prenom", max_length=200)
    adresse = models.CharField("Adresse", max_length=200)
    telephone = models.CharField("telephone", max_length=15, unique=True)
    code_postal = models.CharField("Code postal", max_length=5, blank=True, null=True)
    ville = models.CharField("Ville", max_length=200, blank=True, null=True)
    objet = models.TextField("Objet")
    contenu = SummernoteTextField("Contenu")
    # signature
    status = models.BooleanField("Status", default=False)

    def __str__(self):
        return self.numero_mention


class Perte(models.Model):
    brigade = models.ForeignKey(Brigade, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField("Date", auto_now_add=True)
    numero_mention = models.IntegerField("Numero mention", null=True, blank=True)
    heure = models.TimeField("Heure", auto_now_add=False)
    nom_prenom = models.CharField("Nom et Prenom", max_length=200)
    adresse = models.CharField("Adresse", max_length=200)
    telephone = models.CharField("telephone", max_length=15, unique=True)
    code_postal = models.CharField("Code postal", max_length=5, blank=True, null=True)
    ville = models.CharField("Ville", max_length=200, blank=True, null=True)
    objet = models.TextField("Objet")
    contenu = SummernoteTextField("Contenu")
    status = models.BooleanField("Status", default=False)

    def __str__(self):
        return self.numero_mention


class ObjectConsigne(models.Model):
    nom = models.CharField("Nom", max_length=200)
    description = models.TextField("Description", blank=True, null=True)

    def __str__(self):
        return self.nom


class Ecrou(models.Model):
    brigade = models.ForeignKey(Brigade, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField("Date", auto_now_add=True)
    numero_mention = models.IntegerField("Numero mention", null=True, blank=True)
    heure = models.TimeField("Heure", auto_now_add=False)
    nom_prenom = models.CharField("Nom et Prenom", max_length=200)
    adresse = models.CharField("Adresse", max_length=200)
    telephone = models.CharField("telephone", max_length=15, unique=True)
    code_postal = models.CharField("Code postal", max_length=5, blank=True, null=True)
    ville = models.CharField("Ville", max_length=200, blank=True, null=True)
    objects_consignes = models.ForeignKey(ObjectConsigne, on_delete=models.CASCADE)
    status = models.BooleanField("Status", default=False)

    def __str__(self):
        return self.numero_mention






