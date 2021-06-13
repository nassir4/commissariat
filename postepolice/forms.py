from bootstrap_datepicker_plus import TimePickerInput
from django.forms import ModelForm, TimeField

from postepolice.models import MainCourante, Plainte, Perte, ObjectConsigne, Ecrou


class MainCouranteForm(ModelForm):
    class Meta:
        model = MainCourante
        fields = ['numero_mention','heure','motif']
    heure = TimeField(
            widget=TimePickerInput()
        )
class PlainteForm(ModelForm):
    class Meta:
        model = Plainte
        fields = ['numero_mention','heure','nom_prenom','adresse','ville','code_postal','objet','contenu']
    heure = TimeField(
            widget=TimePickerInput()
        )
class PerteForm(ModelForm):
    class Meta:
        model = Perte
        fields = ['numero_mention','heure','nom_prenom','adresse','ville','code_postal','objet','contenu']
class ObjectConsigneForm(ModelForm):
    class Meta:
        model = ObjectConsigne
        fields = '__all__'
    heure = TimeField(
            widget=TimePickerInput()
        )
class EcrouForm(ModelForm):
    class Meta:
        model =Ecrou
        fields = ['numero_mention','heure','nom_prenom','adresse','ville','code_postal','objects_consignes']
    heure = TimeField(
            widget=TimePickerInput()
        )