from bootstrap_datepicker_plus import TimePickerInput, DatePickerInput
from django.forms import ModelForm, TimeField, DateField

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
class GardeAVueIdentite(ModelForm):
    class Meta:
        model = GardeAVue
        fields = ['numero','nom','prenom','date_naissance','lieu_naissance','profession','domicile']
    date_naissance = DateField(
            widget=DatePickerInput(format='%d/%m/%Y'),
    )

class GardeAVueMotif(ModelForm):
    class Meta:
        model = GardeAVue
        fields = ['motif']
class GardeAVueDecision(ModelForm):
    class Meta:
        model = GardeAVue
        fields = ['prise_par']
class GardeAVueDeroul(ModelForm):
    class Meta:
        model = GardeAVue
        fields = ['date_debut','heure_debut','heure_debut_audition','heure_fin_audition',
                  'duree_audition','heure_debut_repos','heure_fin_repos','duree_repos','liberte',
                  'date_conduite','heure_conduite','devant','numero_pv','date_pv']
    date_debut = DateField(
        widget=DatePickerInput(format='%d/%m/%Y')
    )
    date_conduite = DateField(
       widget=DatePickerInput(format='%d/%m/%Y'),
    )
    date_pv = DateField(
      widget=DatePickerInput(format='%d/%m/%Y'),

    )
    heure_debut = TimeField(
        widget=TimePickerInput()
    )
    heure_debut_audition = TimeField(
       widget=TimePickerInput()
    )
    heure_fin_audition = TimeField(
        widget=TimePickerInput()
    )
    heure_debut_repos = TimeField(
        widget=TimePickerInput()
    )
    heure_fin_repos = TimeField(
       widget=TimePickerInput()
    )
    heure_conduite = TimeField(
        widget=TimePickerInput()
    )

class gardeAVueProl(ModelForm):
    class Meta:
        model= GardeAVue
        fields = ['date_prolongation','heure_prolongation',
                  'aupres_de', 'decision_magistrat']

    heure_prolongation = TimeField(
        widget=TimePickerInput()
    )
    date_prolongation = DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),

    )
class GardeAVueObser(ModelForm):
    class Meta:
        model = GardeAVue
        fields = ['observations']