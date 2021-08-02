from bootstrap_datepicker_plus import TimePickerInput
from django.forms import ModelForm, TimeField

from postepolice.models import MainCourante, Plainte, Perte, ObjectConsigne, Ecrou, Registre, GardeAVue


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
        fields = ['numero_mention','heure','motif','photo1','photo2']
    heure = TimeField(
            widget=TimePickerInput()
        )
class PerteForm(ModelForm):
    class Meta:
        model = Perte
        fields = ['numero_mention','heure','motif']
    heure = TimeField(
        widget=TimePickerInput()
    )
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
        fields = ['numero_mention','heure','petite_identite','objects_consignes','motif_garde_vue','suite']
    heure = TimeField(
            widget=TimePickerInput()
        )
class RegistreForm(ModelForm):
    class Meta:
        model = Registre
        fields = ['brigade']
class GardeAVueForm(ModelForm):
    class Meta:
        model = GardeAVue
        fields = ['numero','nom','prenom','date_naissance','lieu_naissance','profession','domicile']