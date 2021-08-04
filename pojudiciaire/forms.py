from django.contrib.auth.models import User
from django.forms import ModelForm,CharField
from .models import Saisine, Interrogatoire, Audition, Cloture, Confrontation, Mission, Requisition, Notification, \
    Conduite, Crime


class CrimeForm(ModelForm):
    class Meta:
        model=Crime
        fields=['affaire','typeInfraction','incrimination']
class CrimeSecretariat(ModelForm):
    class Meta:
        model=Crime
        fields=['affaire','typeInfraction','incrimination','user']

class SaisineForm(ModelForm):
    class Meta:
        model = Saisine
        fields = ["numeroPv","objet","vuEtTransmis","ouvertureEnquete","description"]
class InterrogatoireForm(ModelForm):
    class Meta:
        model = Interrogatoire
        fields = ["numeroPv","objet","description"]
class AuditionForm(ModelForm):
    class Meta:
        model = Audition
        fields = ["numeroPv","objet","description"]
class ClotureForm(ModelForm):
    class Meta:
        model = Cloture
        fields = ["numeroPv","objet","deroulementEtNotification","controleEtTransmission","mentionRestitution","description"]
class ConfrontationForm(ModelForm):
    class Meta:
        model = Confrontation
        fields = ["numeroPv", "objet", "description"]
class MissionForm(ModelForm):
    class Meta:
        model = Mission
        fields = ["numeroPv", "objet", "description"]
class RequisitionForm(ModelForm):
    class Meta:
        model = Requisition
        fields =["numeroPv","objet","reference","description"]
class ConduiteForm(ModelForm):
    class Meta:
        model = Conduite
        fields = ["numeroPv", "objet", "description"]
class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = ["numeroPv", "objet","description"]

