from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from accident import forms
from accident.forms import TypeAccidentForm, AccidentForm, VehiculeForm, EclairageForm, EssuieGlaceForm, \
    RetroviseurForm, IndicateurVitesseForm, IndicateurDirectionForm, AvertisseurForm, ConducteurForm, VictimeForm, \
    TemoinForm, EtatDesLieuxForm, DeclarationForm, PermisForm, ProprietaireForm, AccidentMaterielForm, \
    VehiculeMaterielForm, AssuranceForm
from accident.models import TypeAccident, Accident, EssuieGlace, Vehicule, Conducteur, Permis, Assurance, Victime, \
    Temoin, EtatDesLieux, Declaration, Proprietaire


def index (request):
    listAccident = Accident.objects.all
    return render(request,'index.html',{'listAccident':listAccident})
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
        listVehicule = Vehicule.objects.filter(accident=accident)
        i=0
        listConducteur=[]
        listAssurance=[]
        listPermis=[]
        listTemoin=Temoin.objects.filter(accident=accident)
        listVictime= Victime.objects.filter(accident=accident)
        etatDesLieux=EtatDesLieux.objects.get(accident=accident)
        listDeclaration=[]
        listProprietaire=[]
        for vehicule in listVehicule:
            listConducteur.append(Conducteur.objects.get(vehicule=vehicule))
        for vehicule in listVehicule:
            listAssurance.append(Assurance.objects.get(vehicule=vehicule))
        for conducteur in listConducteur:
            listPermis.append(Permis.objects.get(conducteur=conducteur))
        for conducteur in listConducteur:
            listDeclaration.append(Declaration.objects.get(conducteur=conducteur))
        for vehicule in listVehicule:
            listProprietaire.append(Proprietaire.objects.get(vehicule=vehicule))
        context = {
            'listProprietaire':listProprietaire,
            'listDeclaration':listDeclaration,
            'listTemoin':listTemoin,
            'listVictime':listVictime,
            'listPermis':listPermis,
            'listAssurance':listAssurance,
            'listConducteur':listConducteur,
            'accident': accident,
            'listVehicule':listVehicule,
            'etatDesLieux':etatDesLieux
        }
    except Accident.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail_accident.html', context)
def modifierAccident(request,accident_id):
    try:
        accident = Accident.objects.get(pk=accident_id)
    except Accident.DoesNotExist:
        return redirect('accident:detail_accident')
    form = AccidentMaterielForm(request.POST or None, instance=accident)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('accident:list_accident')
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_accident.html', context)

def modifierVehicule(request,vehicule_id):
    try:
        vehicule = Vehicule.objects.get(pk=vehicule_id)
    except Vehicule.DoesNotExist:
        return redirect('accident:detail_accident')
    form = VehiculeMaterielForm(request.POST or None, instance=vehicule)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('accident:list_accident')
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_vehicule.html', context)


def modifierConducteur(request,conducteur_id):
    try:
        conducteur = Conducteur.objects.get(pk=conducteur_id)
    except Conducteur.DoesNotExist:
        return redirect('accident:detail_accident')
    form = ConducteurForm(request.POST or None, instance=conducteur)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('accident:list_accident')
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_conducteur.html', context)

def modifierAssurance(request,id):
    try:
        assurance = Assurance.objects.get(pk=id)
    except Assurance.DoesNotExist:
        return redirect('accident:detail_accident')
    form = AssuranceForm(request.POST or None, instance=assurance)
    if form.is_valid():
        form.save()
        return redirect('accident:list_accident')
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_assurance.html', context)

def modifierPermis(request,id):
    try:
      permis = Permis.objects.get(pk=id)
    except Permis.DoesNotExist:
        return redirect('accident:detail_accident')
    form = PermisForm(request.POST or None, instance=permis)
    if form.is_valid():
        form.save()
        return redirect('accident:list_accident')
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_permis.html', context)

def modifierProprietaire(request,id):
    try:
        proprietaire = Proprietaire.objects.get(pk=id)
    except Proprietaire.DoesNotExist:
        return redirect('accident:detail_accident')
    form = ProprietaireForm(request.POST or None, instance=proprietaire)
    if form.is_valid():
        form.save()
        return redirect('accident:list_accident')
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_proprietaire.html', context)

def modifierVictime(request,id):
    try:
        victime = Victime.objects.get(pk=id)
    except Victime.DoesNotExist:
        return redirect('accident:detail_accident')
    form = VictimeForm(request.POST or None, instance=victime)
    if form.is_valid():
        form.save()
        return redirect('accident:list_accident')
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_victime.html', context)

def modifierTemoin(request,id):
    try:
        temoin = Temoin.objects.get(pk=id)
    except Temoin.DoesNotExist:
        return redirect('accident:detail_accident')
    form = TemoinForm(request.POST or None, instance=temoin)
    if form.is_valid():
        form.save()
        return redirect('accident:list_accident')
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_temoin.html', context)
def modifierEtatDesLieux(request,id):
    try:
        etatDesLieux = EtatDesLieux.objects.get(pk=id)
    except EtatDesLieux.DoesNotExist:
        return redirect('accident:detail_accident')
    form = EtatDesLieuxForm(request.POST or None, instance=etatDesLieux)
    if form.is_valid():
        form.save()
        return redirect('accident:list_accident')
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_etat.html', context)

def modifierDeclaration(request,id):
    try:
        declaration = Declaration.objects.get(pk=id)
    except Declaration.DoesNotExist:
        return redirect('accident:detail_accident')
    form =DeclarationForm(request.POST or None, instance=declaration)
    if form.is_valid():
        form.save()
        return redirect('accident:list_accident')
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_declaration.html', context)

def deleteAccident(id):
    accident = Accident.objects.get(pk=id)
    accident.delete()
    return redirect('accident:list_accident')
def deleteVehicule(id):
    vehicule = Vehicule.objects.get(pk=id)
    vehicule.delete()
    return redirect('accident:list_accident')
def deleteConducteur(id):
    conducteur = Conducteur.objects.get(pk=id)
    conducteur.delete()
    return redirect('accident:list_accident')
def deletePermis(id):
    permis = Permis.objects.get(pk=id)
    permis.delete()
    return redirect('accident:list_accident')
def deletePropprietaire(id):
    proprietaire = Proprietaire.objects.get(pk=id)
    proprietaire.delete()
    return redirect('accident:list_accident')
def deleteAssurance(id):
    assurance = Assurance.objects.get(pk=id)
    assurance.delete()
    return redirect('accident:list_accident')
def deleteVictime(id):
    victime = Victime.objects.get(pk=id)
    victime.delete()
    return redirect('accident:list_accident')
def deleteEtatDesLieux(id):
    etatDesLieux = EtatDesLieux.objects.get(pk=id)
    etatDesLieux.delete()
    return redirect('accident:list_accident')
def deleteDeclaraton(id):
    declaration = Declaration.objects.get(pk=id)
    declaration.delete()
    return redirect('accident:list_accident')
def deletetemoin(id):
    temoin = Temoin.objects.get(pk=id)
    temoin.delete()
    return redirect('accident:list_accident')
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
    return  render(request,'accident.html',context)
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
    if request.method == 'POST':
        form = DeclarationForm(request.POST)
        if form.is_valid():
            declaration = form.save(commit=False)
            declaration.save()
            return redirect('/')
    else:
        form = DeclarationForm
    return render(request, 'accident_materiel/enregistrement_declaration.html', {'form': form})
