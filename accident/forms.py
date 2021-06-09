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
        def __init__(self, *args, **kwargs):
            super().__init__(*args, *kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Row(
                    Column('numero_accident',  css_class='form-group col-md-4 mb-0'),
                    Column('date_accident', css_class='form-group col-md-4 mb-0'),
                    Column('heure_accident', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),

                Row(
                    Column('lieu_accident', css_class='form-group col-md-4 mb-0'),
                    Column('type_accident', css_class='form-group col-md-4 mb-0'),
                    Column('etabli_par', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('assiste_de', css_class='form-group col-md-6 mb-0'),
                    Column('mesures_prises', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('circonstances', css_class='form-group col-md-6 mb-0'),
                    Column('infractions_relevees', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('autres_dommages', css_class='form-group col-md-6 mb-0'),
                    Column('derniere_mesures_prises', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Submit('submit', 'Enregister')
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
    def __init__(self,*args,**kwargs):
        super().__init__(*args, *kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('accident', css_class='form-group col-md-3 mb-0'),
                Column('numero', css_class='form-group col-md-3 mb-0'),
                Column('genre', css_class='form-group col-md-3 mb-0'),
                Column('marque', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            'puissance',
            Row(
                Column('charge_total', css_class='form-group col-md-3 mb-0'),
                Column('dimension', css_class='form-group col-md-3 mb-0'),
                Column('date_mise_circulation', css_class='form-group col-md-3 mb-0'),
                Column('derniere_visite_technique', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('kilometrage', css_class='form-group col-md-3 mb-0'),
                Column('etat_general', css_class='form-group col-md-3 mb-0'),
                Column('valeur_systeme_freinage', css_class='form-group col-md-3 mb-0'),
                Column('etat_pneus_avant', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('etat_pneus_arriere', css_class='form-group col-md-4 mb-0'),
                Column('etat_parebrise', css_class='form-group col-md-4 mb-0'),
                Column('degats_materiels', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),

            'position_levier_vitesse',
            'presence_poste_radio',

            Submit('submit', 'Enregister')
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nom_prenom', css_class='form-group col-md-3 mb-0'),
                Column('date_naissance', css_class='form-group col-md-3 mb-0'),
                Column('lieu_naissance', css_class='form-group col-md-3 mb-0'),
                Column('filiation', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('domicile', css_class='form-group col-md-3 mb-0'),
                Column('profession', css_class='form-group col-md-3 mb-0'),
                Column('telephone', css_class='form-group col-md-3 mb-0'),
                Column('comportement', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),

        )
class VictimeForm(ModelForm):
    class Meta:
        model=Victime
        fields=['nom_prenom','filiation_complete','adresse','position_moment_accident','nature_des_blessures']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nom_prenom', css_class='form-group col-md-6 mb-0'),
                Column('filiation_complete', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('adresse', css_class='form-group col-md-6 mb-0'),
                Column('position_moment_accident', css_class='form-group col-md-6 mb-0'),
                css_class='for-row'
            ),
            'nature_des_blessures',
            Submit('submit','Enregistrer')
        )

class TemoinForm(ModelForm):
    class Meta:
        model=Temoin
        fields=['nom_prenom','profession','adresse','position_moment_accident']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nom_prenom', css_class='form-group col-md-6 mb-0'),
                Column('profession', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('adresse', css_class='form-group col-md-6 mb-0'),
                Column('position_moment_accident', css_class='form-group col-md-6 mb-0'),
                css_class='for-row'
            ),
            Submit('submit','Enregistrer')
        )
class EtatDesLieuxForm(ModelForm):
    class Meta:
        model=EtatDesLieux
        fields=['visibilite','chaussee','largeur','eclairage','tracesFreinage','tracesSang','tracePneu','PassagePieton','condition_atmospherique']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper()
        self.helper.layout=Layout(
            Row(
                Column('visibilite', css_class='form-group col-md-3 mb-0'),
                Column('chaussee', css_class='form-group col-md-3 mb-0'),
                Column('largeur', css_class='form-group col-md-3 mb-0'),
                Column('eclairage', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('tracesFreinage', css_class='form-group col-md-3 mb-0'),
                Column('tracesSang', css_class='form-group col-md-3 mb-0'),
                Column('tracePneu', css_class='form-group col-md-3 mb-0'),
                Column('PassagePieton', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            'condition_atmospherique',
            Submit('submit','Enregistrer')
        )

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('numero', css_class='form-group col-md-6 mb-0'),
                Column('delivre_par', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('delivre_le', css_class='form-group col-md-6 mb-0'),
                Column('lieu', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('numero_police', css_class='form-group col-md-6 mb-0'),
                Column('nom', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('date_debut', css_class='form-group col-md-6 mb-0'),
                Column('date_expiration', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
        Row(
            Column('numero_accident', css_class='form-group col-md-4 mb-0'),
            Column('date_accident', css_class='form-group col-md-4 mb-0'),
            Column('heure_accident', css_class='form-group col-md-4 mb-0'),
            css_class='form-row'
        ),

        Row(
            Column('lieu_accident', css_class='form-group col-md-4 mb-0'),
            Column('etabli_par', css_class='form-group col-md-4 mb-0'),
            Column('assiste_de', css_class='form-group col-md-4 mb-0'),
            css_class='form-row'
        ),
        'autres_dommages',
        Submit('submit', 'Enregister')
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
    def __init__(self,*args,**kwargs):
        super().__init__(*args, *kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('numero', css_class='form-group col-md-4 mb-0'),
                Column('genre', css_class='form-group col-md-4 mb-0'),
                Column('marque', css_class='form-group col-md-4 mb-0'),

                css_class='form-row'
            ),

            Row(
                Column('date_mise_circulation', css_class='form-group col-md-6 mb-0'),
                Column('derniere_visite_technique', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )


class DeclarationForm(ModelForm):
    class Meta:
        model=Declaration
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout=Layout(
            Row(
                Column('declaration', css_class='form-group col-md-6 mb-0'),
                Column('infraction', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Enregister')

        )
