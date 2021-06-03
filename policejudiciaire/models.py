import datetime

from django.db import models
from django_summernote.fields import SummernoteTextField
# Create your models here.
class PV (models.Model):
    numeroPv = models.IntegerField()
    objet = models.CharField(max_length=300)
    description = SummernoteTextField( blank=True, null=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.objet
class Saisine (PV):
    affaire = models.CharField(max_length=200)
    incrimination = models.CharField(max_length=100)
    vuEtTransmis = models.BooleanField("Vu et Transmis", default=True)
    ouvertureEnquete = models.BooleanField("Ouverture Enquete",default=True)
class Audition(PV):
    affaire = models.CharField(max_length=200)
    incrimination = models.CharField(max_length=100)
class Notification(PV):
    affaire = models.CharField(max_length=200)
    incrimination = models.CharField(max_length=100)
class Interrogatoire(PV):
    affaire = models.CharField(max_length=200)
    incrimination = models.CharField(max_length=100)
class Conduite(PV):
    affaire = models.CharField(max_length=200)
    incrimination = models.CharField(max_length=100)
class Confrontation(PV):
    affaire = models.CharField(max_length=200)
    incrimination = models.CharField(max_length=100)
class Mission(PV):
    affaire = models.CharField(max_length=200)
    incrimination = models.CharField(max_length=100)
class Cloture(PV):
    affaire = models.CharField(max_length=200)
    incrimination = models.CharField(max_length=100)
    deroulementEtNotification = models.BooleanField(True)
    controleEtTransmission = models.BooleanField(True)
    mentionRestitution = models.BooleanField(True)
class Requisition(PV):
    reference=models.CharField(max_length=200)