from django.forms import ModelForm,CharField
from .models import Saisine, Interrogatoire, Audition, Cloture, Confrontation, Mission, Requisition, Notification, \
    Conduite


class SaisineForm(ModelForm):
    class Meta:
        model = Saisine
        fields = ["numeroPv","objet","affaire","vuEtTransmis","ouvertureEnquete","incrimination","description"]
class InterrogatoireForm(ModelForm):
    class Meta:
        model = Interrogatoire
        fields = ["numeroPv","objet","affaire","incrimination","description"]
class AuditionForm(ModelForm):
    class Meta:
        model = Audition
        fields = ["numeroPv","objet","affaire","incrimination","description"]
class ClotureForm(ModelForm):
    class Meta:
        model = Cloture
        fields = ["numeroPv","objet","affaire","incrimination","deroulementEtNotification","controleEtTransmission","mentionRestitution","description"]
class ConfrontationForm(ModelForm):
    class Meta:
        model = Confrontation
        fields = ["numeroPv", "objet", "affaire", "incrimination", "description"]
class MissionForm(ModelForm):
    class Meta:
        model = Mission
        fields = ["numeroPv", "objet", "affaire", "incrimination", "description"]
class RequisitionForm(ModelForm):
    class Meta:
        model = Requisition
        fields =["numeroPv","objet","reference","description"]
class ConduiteForm(ModelForm):
    class Meta:
        model = Conduite
        fields = ["numeroPv", "objet", "affaire", "incrimination", "description"]
class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = ["numeroPv", "objet", "affaire", "incrimination", "description"]

