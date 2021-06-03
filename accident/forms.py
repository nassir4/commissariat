from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.forms import ModelForm, DateField, TimeField

from accident.models import TypeAccident, Accident, Vehicule, Eclairage, Avertisseur, IndicateurDirection, \
    IndicateurVitesse, EssuieGlace, Retroviseur, Conducteur, Victime, Temoin, EtatDesLieux, Declaration


class TypeAccidentForm(ModelForm):
    class Meta:
        model = TypeAccident
        fields=["nom", "description"]
class AccidentForm(ModelForm):
        class Meta:
            model = Accident
            fields= '__all__'

        date_accident = DateField(
            widget=DatePickerInput(format='%m/%d/%Y'),

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
        widget=DatePickerInput(format='%m/%d/%Y'),

    )
    derniere_visite_technique = DateField(
        widget=DatePickerInput(format='%m/%d/%Y'),

    )
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('accident', css_class='form-group col-md-3 mb-0'),
                Column('numero', css_class='form-group col-md-3 mb-0'),
                Column('genre', css_class='form-group col-md-3 mb-0'),
                Column('marque', css_class='form-group col-md-3 mb-0'),
                Column('puisssance', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
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
        fields = '__all__'

    date_naissance = DateField(
        widget=DatePickerInput(format='%m/%d/%Y'),

    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'vehicule',
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
            Submit('submit', 'Enregistrer')

        )
class VictimeForm(ModelForm):
    class Meta:
        model=Victime
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper()
        self.helper.layout = Layout(
            'accident',
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
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper()
        self.helper.layout = Layout(
            'accident',
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
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper()
        self.helper.layout=Layout(
            'accident',
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
class DeclarationForm(ModelForm):
    class Meta:
        model=Declaration
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout=Layout(
            'conducteur',
            Row(
                Column('declaration', css_class='form-group col-md-6 mb-0'),
                Column('infraction', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Enregistrer')

        )
