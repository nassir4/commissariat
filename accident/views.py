from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from accident import forms
from accident.forms import TypeAccidentForm, AccidentForm, VehiculeForm, EclairageForm, EssuieGlaceForm, \
    RetroviseurForm, IndicateurVitesseForm, IndicateurDirectionForm, AvertisseurForm, ConducteurForm, VictimeForm, \
    TemoinForm, EtatDesLieuxForm, DeclarationForm, PermisForm, ProprietaireForm, AccidentMaterielForm, \
    VehiculeMaterielForm, AssuranceForm
from accident.models import TypeAccident, Accident, EssuieGlace, Vehicule, Conducteur, Permis
from accident.multiple_forms import MultipleFormsView


def index (request):
    return render(request,'index.html')
### Type Accident ###
def typeAccident(request):
    listTypeAccident = TypeAccident.objects.all
    context = {
        'listTypeAccident': listTypeAccident
    }
    return render(request, 'type_accident.html',context);
def detailTypeAccident(request, pv_id):
    try:
        typeAccident = TypeAccident.objects.get(pk=pv_id)
    except TypeAccident.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail_type_accident.html', {'typeAccident': typeAccident})

def save(request):
    form = TypeAccidentForm
    if request.method == 'POST':
        form =TypeAccidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accident:type_accident')
    else:
        form = TypeAccidentForm
    return render(request, 'enregistrement_type_accident.html',{'form':form})
def update(request,type_id):
    try:
        typeAccident = TypeAccident.objects.get(pk=type_id)
    except TypeAccident.DoesNotExist:
        return redirect('accident:detail_type_accident')
    form = TypeAccidentForm(request.POST or None, instance=typeAccident)
    if form.is_valid():
        form.save()
        return redirect('accident:type_accident')
    context = {
        'form': form,
    }
    return render(request, 'enregistrement_type_accident.html',context)
def delete(request,type_id):
    typeAccident = TypeAccident.objects.get(pk=type_id)
    typeAccident.delete()
    return redirect('accident:type_accident')
### Fin Type Accident ####

###########################################################################################################
############################################## ACCIDENT CORPOREL ##########################################
###########################################################################################################
### Accident ###
def accident(request):
    listaccident = Accident.objects.all
    context = {
        'listAccident': listaccident
    }
    return render(request, 'accident.html',context);
def detailAccident(request, accident_id):
    try:
        accident = Accident.objects.get(pk=accident_id)
    except Accident.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail_accident.html', {'accident': accident})

##########################################################################################################################
############################################ FIN ACCIDENT CORPOREL #######################################################
##########################################################################################################################


##########################################################################################################################
############################################ ACCIDENT MATERIEL ###########################################################
##########################################################################################################################

# Vue Accident Corporel
def accidentMateriel(request):
    accident = Accident.objects.last()
    listVehicule=Vehicule.objects.filter(accident=accident)
    vehicule1 = listVehicule[0]
    conducteur1=Conducteur.objects.get(vehicule=vehicule1)
    permis=Permis.objects.get(conducteur=conducteur1)

    #conducteur2=Conducteur.objects.filter(vehicule=listVehicule[1])
    context = {
        'accident':accident,
        'vehicule1':vehicule1,
        'conducteur1':conducteur1,
        'permis':permis
       # 'conducteur':conducteur2,
    }
    return  render(request,'accident_materiel.html',context)
#Fin Vue Accident Materiel
def saveAccidentMateriel(request):
    typeAccident=TypeAccident.objects.get(nom='Accident Materiel')
    if request.method == 'POST':
        form =AccidentMaterielForm(request.POST)
        if form.is_valid():
            accident = form.save(commit=False)
            accident.type_accident=typeAccident
            accident.save()
            return redirect('accident:vehicule_materiel_save')
    else:
        form = AccidentMaterielForm
    return render(request, 'accident_materiel/enregistrement_accident.html', {'form': form})

def vehiculeMatertielSave(request):
    accident = Accident.objects.last()
    if request.method == 'POST':
        vehicule_form = VehiculeMaterielForm(request.POST)
        assurance_form = AssuranceForm(request.POST)
        proprietaire_form = ProprietaireForm(request.POST)
        conducteur_form = ConducteurForm(request.POST)
        permis_form = PermisForm(request.POST)
        if (vehicule_form.is_valid() and assurance_form.is_valid() and proprietaire_form.is_valid()
                and conducteur_form.is_valid() and permis_form.is_valid()):
            vehicule = vehicule_form.save(commit=False)
            vehicule.accident = accident
            ve = vehicule.save()
            assurance = assurance_form.save(commit=False)
            assurance.vehicule= ve
            assurance.save()
            proprietaire = proprietaire_form.save(commit=False)
            proprietaire.vehicule =ve
            proprietaire.save()
            conducteur = conducteur_form.save(commit=False)
            conducteur.vehicule=ve
            con=conducteur.save()
            permis =permis_form.save(commit=False)
            permis.conducteur=con
            permis.save()
            return redirect('accident:temoin_materiel_save')
    else:
        vehicule_form = VehiculeMaterielForm
        assurance_form = AssuranceForm
        proprietaire_form = ProprietaireForm
        conducteur_form = ConducteurForm
        permis_form = PermisForm

    return render(request, 'accident_materiel/enregistrement.html', {'vehicule_form': vehicule_form,
                                                                                'assurance_form': assurance_form,
                                                                                'proprietaire_form': proprietaire_form,
                                                                                'conducteur_form': conducteur_form,
                                                                                'permis_form': permis_form,
                                                                                })
def temoinMaterielSave(request):
    accident=Accident.objects.last()
    if request.method == 'POST':
        form =TemoinForm(request.POST)
        if form.is_valid():
            temoin = form.save(commit=False)
            temoin.accident=accident
            temoin.save()
            return redirect('accident:temoin_materiel_save')
    else:
        form = TemoinForm
    return render(request, 'accident_materiel/enregistrement_temoin.html', {'form': form})
def temoinEndSave(request):
    accident = Accident.objects.last()
    if request.method == 'POST':
        form = TemoinForm(request.POST)
        if form.is_valid():
            temoin = form.save(commit=False)
            temoin.accident = accident
            temoin.save()
            return redirect('accident:victime_materiel_save')
    else:
        form = TemoinForm
    return render(request, 'accident_materiel/enregistrement_temoin.html', {'form': form})
def victimeMaterielSave(request):
    accident = Accident.objects.last()
    if request.method == 'POST':
        form = VictimeForm(request.POST)
        if form.is_valid():
            victime = form.save(commit=False)
            victime.accident = accident
            victime.save()
            return redirect('accident:etat_materiel_save')
    else:
        form = VictimeForm
    return render(request, 'accident_materiel/enregistrement_victime.html', {'form': form})

def victimeEndSave(request):
    accident = Accident.objects.last()
    if request.method == 'POST':
        form = VictimeForm(request.POST)
        if form.is_valid():
            victime = form.save(commit=False)
            victime.accident = accident
            victime.save()
            return redirect('accident:accident_materiel_save')
    else:
        form = VictimeForm
    return render(request, 'accident_materiel/enregistrement_temoin.html', {'form': form})
def etatSave(request):
    accident = Accident.objects.last()
    if request.method == 'POST':
        form = EtatDesLieuxForm(request.POST)
        if form.is_valid():
            etat = form.save(commit=False)
            etat.accident = accident
            etat.save()
            return redirect('accident:declaration_materiel_save')
    else:
        form = EtatDesLieuxForm
    return render(request, 'accident_materiel/enregistrement_etat.html', {'form': form})
def declarationSave(request):
    accident = Accident.objects.last()
    if request.method == 'POST':
        form = DeclarationForm(request.POST)
        if form.is_valid():
            declaration = form.save(commit=False)
            declaration.accident = accident
            declaration.save()
            return redirect('/')
    else:
        form = DeclarationForm
    return render(request, 'accident_materiel/enregistrement_declaration.html', {'form': form})