import datetime

from django.db import models
from django_summernote.fields import SummernoteTextField
# Create your models here.
class Crime(models.Model):
    affaire = models.CharField(max_length=200)
    incrimination = models.CharField(max_length=100)
    def __str__(self):
        return self.affaire
class Saisine (models.Model):
    numeroPv = models.IntegerField(blank=True, null=True)
    objet = models.CharField(max_length=300,blank=True, null=True)
    description = SummernoteTextField(blank=True, null=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    vuEtTransmis = models.BooleanField("Vu et Transmis", default=False,blank=True, null=True)
    ouvertureEnquete = models.BooleanField("Ouverture Enquete",default=False,blank=True, null=True)
    crime = models.ForeignKey(Crime, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.objet
class Audition(models.Model):
    numeroPv = models.IntegerField(blank=True, null=True)
    objet = models.CharField(max_length=300,blank=True, null=True)
    description = SummernoteTextField(blank=True, null=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    crime = models.ForeignKey(Crime, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.objet
class Notification(models.Model):
    numeroPv = models.IntegerField(blank=True, null=True)
    objet = models.CharField(max_length=300,blank=True, null=True)
    description = SummernoteTextField(blank=True, null=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    crime = models.ForeignKey(Crime, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.objet
class Interrogatoire(models.Model):
    numeroPv = models.IntegerField(blank=True, null=True)
    objet = models.CharField(max_length=300,blank=True, null=True)
    description = SummernoteTextField(blank=True, null=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    crime = models.ForeignKey(Crime, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.objet
class Conduite(models.Model):
    numeroPv = models.IntegerField(blank=True, null=True)
    objet = models.CharField(max_length=300,blank=True, null=True)
    description = SummernoteTextField(blank=True, null=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    crime = models.ForeignKey(Crime, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.objet
class Confrontation(models.Model):
    numeroPv = models.IntegerField(blank=True, null=True)
    objet = models.CharField(max_length=300,blank=True, null=True)
    description = SummernoteTextField(blank=True, null=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    crime = models.ForeignKey(Crime, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.objet
class Mission(models.Model):
    numeroPv = models.IntegerField(blank=True, null=True)
    objet = models.CharField(max_length=300,blank=True, null=True)
    description = SummernoteTextField(blank=True, null=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    crime = models.ForeignKey(Crime, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.objet
class Cloture(models.Model):
    numeroPv = models.IntegerField(blank=True, null=True)
    objet = models.CharField(max_length=300,blank=True, null=True)
    description = SummernoteTextField(blank=True, null=True)
    dateCreation = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deroulementEtNotification = models.BooleanField("Deroulement et Notification",default=False,blank=True, null=True)
    controleEtTransmission = models.BooleanField("Controle et Transmission",default=False,blank=True, null=True)
    mentionRestitution = models.BooleanField("Mention et Restition",default=False,blank=True, null=True)
    crime = models.ForeignKey(Crime, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.objet
class Requisition(models.Model):
    numeroPv = models.IntegerField(blank=True, null=True)
    objet = models.CharField(max_length=300,blank=True, null=True)
    description = SummernoteTextField(blank=True, null=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    reference=models.CharField(max_length=200,blank=True, null=True)
    crime = models.ForeignKey(Crime, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.objet