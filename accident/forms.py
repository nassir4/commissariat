from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.forms import ModelForm, DateField, TimeField

from accident.models import TypeAccident, Accident, Vehicule, Eclairage, Avertisseur, IndicateurDirection, \
    IndicateurVitesse, EssuieGlace, Retroviseur, Conducteur, Victime, Temoin, EtatDesLieux, Declaration, Proprietaire, \
    Permis, Assurance


class TypeAccidentForm(ModelForm):
    class Meta:
        model = TypeAccident
        fields=["nom", "description"]
############################################################################################################################
##################################################### Accident Corporel ####################################################
############################################################################################################################
class AccidentForm(ModelForm):
        class Meta:
            model = Accident
            fields= '__all__'

        date_accident = DateField(
            widget=DatePickerInput(format='%d/%m/%Y'),

        )
        heure_accident = TimeField(
            widget=TimePickerInput()
        )

class VehiculeForm(ModelForm):
    class Meta:
        model = Vehicule
        fields = '__all__'

    date_mise_circulation = DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),

    )
    derniere_visite_technique = DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),

    )

class EclairageForm(ModelForm):
    class Meta:
        model = Eclairage
        fields = '__all__'
class AvertisseurForm(ModelForm):
    class Meta:
        model = Avertisseur
        fields = '__all__'
class IndicateurDirectionForm(ModelForm):
    class Meta:
        model = IndicateurDirection
        fields = '__all__'
class IndicateurVitesseForm(ModelForm):
    class Meta:
        model = IndicateurVitesse
        fields = '__all__'
class EssuieGlaceForm(ModelForm):
    class Meta:
        model = EssuieGlace
        fields = '__all__'
class RetroviseurForm(ModelForm):
    class Meta:
        model = Retroviseur
        fields = '__all__'
class ConducteurForm(ModelForm):
    class Meta:
        model = Conducteur
        fields = ['nom_prenom','date_naissance','lieu_naissance','filiation','domicile','profession','telephone','comportement']

    date_naissance = DateField(
        widget=DatePickerInput(format='%m/%d/%Y'),

    )
class VictimeForm(ModelForm):
    class Meta:
        model=Victime
        fields=['nom_prenom','filiation_complete','adresse','position_moment_accident','nature_des_blessures']


class TemoinForm(ModelForm):
    class Meta:
        model=Temoin
        fields=['nom_prenom','profession','adresse','position_moment_accident']


class EtatDesLieuxForm(ModelForm):
    class Meta:
        model=EtatDesLieux
        fields=['visibilite','chaussee','largeur','eclairage','tracesFreinage','tracesSang','tracePneu','PassagePieton','condition_atmospherique']


class ProprietaireForm(ModelForm):
    class Meta:
        model = Proprietaire
        fields = ['nom_prenom','domicile']

class PermisForm(ModelForm):
    class Meta:
        model = Permis
        fields = ['numero','delivre_par','delivre_le','lieu']

    delivre_le = DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),

    )

class AssuranceForm(ModelForm):
    class Meta:
        model = Assurance
        fields= ['numero_police','nom','date_debut','date_expiration']

    date_debut = DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),

    )
    date_expiration = DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),

    )

###########################################################################################################################
#################################################### Fin Accident Corporel ################################################
###########################################################################################################################

###########################################################################################################################
################################################### Accident Materiel #####################################################
###########################################################################################################################

class AccidentMaterielForm(ModelForm):
    class Meta:
        model = Accident
        fields = ['numero_accident','date_accident','heure_accident',
                    'lieu_accident','etabli_par','assiste_de','autres_dommages']

    date_accident = DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),

    )
    heure_accident = TimeField(
        widget=TimePickerInput()
    )
class VehiculeMaterielForm(ModelForm):
    class Meta:
        model = Vehicule
        fields = ['numero','genre','marque','date_mise_circulation','derniere_visite_technique']

    date_mise_circulation = DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),

    )
    derniere_visite_technique = DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),

    )


class DeclarationForm(ModelForm):
    class Meta:
        model=Declaration
        fields='__all__'
