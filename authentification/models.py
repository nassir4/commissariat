from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# departement models
class Departement(models.Model):
    nom = models.CharField("Nom", max_length=255, unique=True)
    description = models.TextField("Description", blank=True)

    def __str__(self):
        return self.nom


# agent models
class Agent(models.Model):
    matricule = models.CharField("Matricule", max_length=10, unique=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField("Telephone", max_length=15, unique=True)
    adresse = models.CharField("Adresse", max_length=255, blank=True)
    grade = models.CharField("Grade", max_length=255, blank=True)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name}-{self.user.last_name}'
