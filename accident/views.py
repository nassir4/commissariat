from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from accident import forms
from accident.forms import TypeAccidentForm, AccidentForm, VehiculeForm, EclairageForm, EssuieGlaceForm, \
    RetroviseurForm, IndicateurVitesseForm, IndicateurDirectionForm, AvertisseurForm, ConducteurForm, VictimeForm, \
    TemoinForm, EtatDesLieuxForm, DeclarationForm, PermisForm, ProprietaireForm, AccidentMaterielForm, \
    VehiculeMaterielForm, AssuranceForm, PVForm
from accident.models import TypeAccident, Accident, EssuieGlace, Vehicule, Conducteur, Permis, Assurance, Victime, \
    Temoin, EtatDesLieux, Declaration, Proprietaire, Eclairage, IndicateurDirection, Avertisseur, IndicateurVitesse, \
    PV
from authentification.decorators import allowed_user


@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def index (request):
    listAccident = Accident.objects.all
    return render(request,'index.html',{'listAccident':listAccident})
### Type Accident ###
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def typeAccident(request):
    listTypeAccident = TypeAccident.objects.all
    context = {
        'listTypeAccident': listTypeAccident
    }
    return render(request, 'type_accident.html',context);
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def detailTypeAccident(request, pv_id):
    try:
        typeAccident = TypeAccident.objects.get(pk=pv_id)
    except TypeAccident.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail_type_accident.html', {'typeAccident': typeAccident})
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
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
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
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
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def delete(request,type_id):
    typeAccident = TypeAccident.objects.get(pk=type_id)
    typeAccident.delete()
    return redirect('accident:type_accident')
### Fin Type Accident ####

###########################################################################################################
############################################## ACCIDENT CORPOREL ##########################################
###########################################################################################################
### Accident ###
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def accident(request):
    listaccident = Accident.objects.all
    context = {
        'listAccident': listaccident
    }
    return render(request, 'accident.html',context);
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def detailAccident(request, accident_id):
    try:
        accidentCorporel = True
        accident = Accident.objects.get(pk=accident_id)
        listVehicule = Vehicule.objects.filter(accident=accident)
        listConducteur=[]
        listAssurance=[]
        listPermis=[]
        listTemoin=Temoin.objects.filter(accident=accident)
        listVictime= Victime.objects.filter(accident=accident)
        etatDesLieux=EtatDesLieux.objects.filter(accident=accident)
        listProprietaire=[]
        listEclairage = []
        listDirection = []
        listAvertisseur=[]
        listVitesse=[]
        listEssuieGlace=[]
        listDeclaration = []
        for conducteur in listConducteur:
            listDeclaration.append(Declaration.objects.get(conducteur=conducteur))
        for vehicule in listVehicule:
            listConducteur.append(Conducteur.objects.get(vehicule=vehicule))
        for vehicule in listVehicule:
            listAssurance.append(Assurance.objects.get(vehicule=vehicule))
        for conducteur in listConducteur:
            listPermis.append(Permis.objects.get(conducteur=conducteur))
        for vehicule in listVehicule:
            listProprietaire.append(Proprietaire.objects.get(vehicule=vehicule))
        if accident.type_accident.nom =="Accident Materiel":
            accidentCorporel = False
        if accident.type_accident.nom =="Accident Corporel":
            for vehicule in listVehicule:
                listEclairage.append(Eclairage.objects.get(vehicule=vehicule))
            for vehicule in listVehicule:
                listDirection.append(IndicateurDirection.objects.get(vehicule=vehicule))
            for vehicule in listVehicule:
                listAvertisseur.append(Avertisseur.objects.get(vehicule=vehicule))
            for vehicule in listVehicule:
                listVitesse.append(IndicateurVitesse.objects.get(vehicule=vehicule))
            for vehicule in listVehicule:
                listEssuieGlace.append(EssuieGlace.objects.get(vehicule=vehicule))

        context = {
            'accidentCorporel':accidentCorporel,
            'listProprietaire':listProprietaire,
            'listDeclaration':listDeclaration,
            'listTemoin':listTemoin,
            'listVictime':listVictime,
            'listPermis':listPermis,
            'listAssurance':listAssurance,
            'listConducteur':listConducteur,
            'accident': accident,
            'listVehicule':listVehicule,
            'etatDesLieux':etatDesLieux,
            'listVitesse':listVitesse,
            'listDirection':listDirection,
            'listAvertisseur':listAvertisseur,
            'listEclairage':listEclairage,
            'listEssuieGlace':listEssuieGlace
        }
    except Accident.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail_accident.html', context)
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierAccident(request,accident_id):
    try:
        accident = Accident.objects.get(pk=accident_id)
    except Accident.DoesNotExist:
        return redirect('accident:detail_accident')
    form = AccidentForm(request.POST or None, instance=accident)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',accident_id=accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_accident.html', context)

@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierVehicule(request,vehicule_id):
    try:
        vehicule = Vehicule.objects.get(pk=vehicule_id)
    except Vehicule.DoesNotExist:
        return redirect('accident:detail_accident')
    form = VehiculeForm(request.POST or None, instance=vehicule)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',accident_id=vehicule.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_vehicule.html', context)


@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierConducteur(request,conducteur_id):
    try:
        conducteur = Conducteur.objects.get(pk=conducteur_id)
    except Conducteur.DoesNotExist:
        return redirect('accident:detail_accident')
    form = ConducteurForm(request.POST or None, instance=conducteur)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',accident_id=conducteur.vehicule.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_conducteur.html', context)

@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierAssurance(request,id):
    try:
        assurance = Assurance.objects.get(pk=id)
    except Assurance.DoesNotExist:
        return redirect('accident:detail_accident')
    form = AssuranceForm(request.POST or None, instance=assurance)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',accident_id=assurance.vehicule.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_assurance.html', context)

@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierPermis(request,id):
    try:
      permis = Permis.objects.get(pk=id)
    except Permis.DoesNotExist:
        return redirect('accident:detail_accident')
    form = PermisForm(request.POST or None, instance=permis)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',permis.conducteur.vehicule.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_permis.html', context)

@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierProprietaire(request,id):
    try:
        proprietaire = Proprietaire.objects.get(pk=id)
    except Proprietaire.DoesNotExist:
        return redirect('accident:detail_accident')
    form = ProprietaireForm(request.POST or None, instance=proprietaire)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',accident_id=proprietaire.vehicule.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_proprietaire.html', context)

@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierVictime(request,id):
    try:
        victime = Victime.objects.get(pk=id)
    except Victime.DoesNotExist:
        return redirect('accident:detail_accident')
    form = VictimeForm(request.POST or None, instance=victime)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',accident_id=victime.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_victime.html', context)

@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierTemoin(request,id):
    try:
        temoin = Temoin.objects.get(pk=id)
    except Temoin.DoesNotExist:
        return redirect('accident:detail_accident')
    form = TemoinForm(request.POST or None, instance=temoin)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',accident_id=temoin.vehicule.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_temoin.html', context)
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierEtatDesLieux(request,id):
    try:
        etatDesLieux = EtatDesLieux.objects.get(pk=id)
    except EtatDesLieux.DoesNotExist:
        return redirect('accident:detail_accident')
    form = EtatDesLieuxForm(request.POST or None, instance=etatDesLieux)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',accident_id=etatDesLieux.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_etat.html', context)

@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierDeclaration(request,id):
    try:
        declaration = Declaration.objects.get(pk=id)
    except Declaration.DoesNotExist:
        return redirect('accident:detail_accident')
    form =DeclarationForm(request.POST or None, instance=declaration)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',accident_id=declaration.conducteur.vehicule.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_materiel/enregistrement_declaration.html', context)
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierVitesse(request,id):
    try:
        vitesse = IndicateurVitesse.objects.get(pk=id)
    except IndicateurVitesse.DoesNotExist:
        return redirect('accident:detail_accident')
    form =IndicateurVitesseForm(request.POST or None, instance=vitesse)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',accident_id=vitesse.vehicule.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_corporel/enregistrement_vitesse.html', context)
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierAvertisseur(request,id):
    try:
        avertisseur = Avertisseur.objects.get(pk=id)
    except Avertisseur.DoesNotExist:
        return redirect('accident:detail_accident')
    form =AvertisseurForm(request.POST or None, instance=avertisseur)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',accident_id=avertisseur.vehicule.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_corporel/enregistrement_avertisseur.html', context)
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierDirection(request,id):
    try:
        direction = IndicateurDirection.objects.get(pk=id)
    except IndicateurDirection.DoesNotExist:
        return redirect('accident:detail_accident')
    form =IndicateurDirectionForm(request.POST or None, instance=direction)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',accident_id=direction.vehicule.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_corporel/enregistrement_direction.html', context)
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierEclairage(request,id):
    try:
        eclairage = Eclairage.objects.get(pk=id)
    except Eclairage.DoesNotExist:
        return redirect('accident:detail_accident')
    form =EclairageForm(request.POST or None, instance=eclairage)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',accident_id=eclairage.vehicule.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_corporel/enregistrement_eclairage.html', context)
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def modifierEssuieGlace(request,id):
    try:
        essuieGlace = EssuieGlace.objects.get(pk=id)
    except EssuieGlace.DoesNotExist:
        return redirect('accident:detail_accident')
    form =EssuieGlaceForm(request.POST or None, instance=essuieGlace)
    if form.is_valid():
        form.save()
        return redirect('accident:detail_accident',essuieGlace.vehicule.accident.id)
    context = {
        'form': form,
    }
    return render(request, 'accident_corporel/enregistrement_essuie_glace.html', context)
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def deleteAccident(id):
    accident = Accident.objects.get(pk=id)
    accident.delete()
    return redirect('accident:list_accident')

##########################################################################################################################
############################################ FIN ACCIDENT CORPOREL #######################################################
##########################################################################################################################


##########################################################################################################################
############################################ ACCIDENT MATERIEL ###########################################################
##########################################################################################################################

# Vue Accident Corporel
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
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
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def saveAccidentMateriel(request):
    typeAccident=TypeAccident.objects.get(nom='Accident Materiel')
    if request.method == 'POST':
        form =AccidentMaterielForm(request.POST)
        if form.is_valid():
            accident = form.save(commit=False)
            accident.type_accident=typeAccident
            accident.save()
            return redirect('accident:detail_accident', accident_id=accident.id)
    else:
        form = AccidentMaterielForm
    return render(request, 'accident_materiel/enregistrement_accident.html', {'form': form})

@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
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
            vehicule.save()
            ve = Vehicule.objects.last()
            assurance = assurance_form.save(commit=False)
            assurance.vehicule= ve
            assurance.save()
            proprietaire = proprietaire_form.save(commit=False)
            proprietaire.vehicule =ve
            proprietaire.save()
            conducteur = conducteur_form.save(commit=False)
            conducteur.vehicule=ve
            conducteur.save()
            con = Conducteur.objects.last()
            permis =permis_form.save(commit=False)
            permis.conducteur=con
            permis.save()
            return redirect('accident:detail_accident',accident_id=accident.id)
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
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def vehiculeCorporelSave(request):
    accident = Accident.objects.last()
    if request.method == 'POST':
        vehicule_form = VehiculeForm(request.POST)
        assurance_form = AssuranceForm(request.POST)
        proprietaire_form = ProprietaireForm(request.POST)
        conducteur_form = ConducteurForm(request.POST)
        permis_form = PermisForm(request.POST)
        eclairage_form = EclairageForm(request.POST)
        vitesse_form=IndicateurVitesseForm(request.POST)
        direction_form =IndicateurDirectionForm(request.POST)
        essuieGlace_form=EssuieGlaceForm(request.POST)
        avertisseur_form=AvertisseurForm(request.POST)

        if (vehicule_form.is_valid() and assurance_form.is_valid() and proprietaire_form.is_valid()
                and conducteur_form.is_valid() and permis_form.is_valid() and eclairage_form.is_valid() and
                vitesse_form.is_valid() and direction_form.is_valid() and essuieGlace_form.is_valid() and
                avertisseur_form.is_valid):
            vehicule = vehicule_form.save(commit=False)
            vehicule.accident = accident
            vehicule.save()
            ve = Vehicule.objects.last()
            eclairage= eclairage_form.save(commit=False)
            eclairage.vehicule=ve
            eclairage.save()
            essuieGlace = essuieGlace_form.save(commit=False)
            essuieGlace.vehicule = ve
            essuieGlace.save()
            direction = direction_form.save(commit=False)
            direction.vehicule = ve
            direction.save()
            avertiseur = avertisseur_form.save(commit=False)
            avertiseur.vehicule = ve
            avertiseur.save()
            vitesse = vitesse_form.save(commit=False)
            vitesse.vehicule = ve
            vitesse.save()
            assurance = assurance_form.save(commit=False)
            assurance.vehicule= ve
            assurance.save()
            proprietaire = proprietaire_form.save(commit=False)
            proprietaire.vehicule =ve
            proprietaire.save()
            conducteur = conducteur_form.save(commit=False)
            conducteur.vehicule=ve
            conducteur.save()
            con = Conducteur.objects.last()
            permis =permis_form.save(commit=False)
            permis.conducteur=con
            permis.save()
            return redirect('accident:detail_accident',accident_id=accident.id)
    else:
        vehicule_form = VehiculeForm
        assurance_form = AssuranceForm
        proprietaire_form = ProprietaireForm
        conducteur_form = ConducteurForm
        permis_form = PermisForm
        eclairage_form = EclairageForm
        vitesse_form = IndicateurVitesseForm
        direction_form = IndicateurDirectionForm
        essuieGlace_form = EssuieGlaceForm
        avertisseur_form = AvertisseurForm
    context = {
        'vehicule_form': vehicule_form,
        'assurance_form': assurance_form,
        'proprietaire_form': proprietaire_form,
        'conducteur_form': conducteur_form,
        'permis_form': permis_form,
        'eclairage_form':eclairage_form,
        'vitesse_form':vitesse_form,
        'direction_form':direction_form,
        'essuieGlace_form':essuieGlace_form,
        'avertisseur_form':avertisseur_form,
    }
    return render(request, 'accident_corporel/enregistrement.html', context)

@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def saveAccidentCorporel(request):
    typeAccident=TypeAccident.objects.get(nom='Accident Corporel')
    if request.method == 'POST':
        form =AccidentForm(request.POST)
        if form.is_valid():
            accident = form.save(commit=False)
            accident.type_accident=typeAccident
            accident.save()
            return redirect('accident:detail_accident',accident_id=accident.id)
    else:
        form = AccidentForm
    return render(request, 'accident_corporel/enregistrement_accident.html', {'form': form})


@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def temoinMaterielSave(request,id):
    accident=Accident.objects.get(pk=id)
    if request.method == 'POST':
        form =TemoinForm(request.POST)
        if form.is_valid():
            temoin = form.save(commit=False)
            temoin.accident=accident
            temoin.save()
            return redirect('accident:detail_accident',accident_id=accident.id)
    else:
        form = TemoinForm
    return render(request, 'accident_materiel/enregistrement_temoin.html', {'form': form})
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def victimeMaterielSave(request,id):
    accident = Accident.objects.get(pk=id)
    if request.method == 'POST':
        form = VictimeForm(request.POST)
        if form.is_valid():
            victime = form.save(commit=False)
            victime.accident = accident
            victime.save()
            return redirect('accident:detail_accident',accident_id=accident.id)
    else:
        form = VictimeForm
    return render(request, 'accident_materiel/enregistrement_victime.html', {'form': form})

@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def etatSave(request,id):
    accident = Accident.objects.get(pk=id)
    if request.method == 'POST':
        form = EtatDesLieuxForm(request.POST)
        if form.is_valid():
            etat = form.save(commit=False)
            etat.accident = accident
            etat.save()
            return redirect('accident:detail_accident',accident_id=accident.id)
    else:
        form = EtatDesLieuxForm
    return render(request, 'accident_materiel/enregistrement_etat.html', {'form': form})
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def declarationSave(request):
    if request.method == 'POST':
        form = DeclarationForm(request.POST)
        if form.is_valid():
            declaration = form.save(commit=False)
            declaration.save()
            return redirect('accident:list_accident')
    else:
        form = DeclarationForm
    return render(request, 'accident_materiel/enregistrement_declaration.html', {'form': form})





"""Saisine"""
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])

def saisine(request):
    listSaisine = PV.objects.all
    context = {
        'listSaisine': listSaisine
    }
    return render(request, 'pv/saisine/saisine.html',context);
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def detailSaisine(request, pv_id):
    try:
        pv = PV.objects.get(pk=pv_id)
    except PV.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'pv/saisine/detail_saisine.html', {'pv': pv})

@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def save(request):
    if request.method == 'POST':
        form = PVForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accident:saisine')
    else:
        form = PVForm
    return render(request, 'pv/saisine/enregistrement.html',{'form':form})
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def update(request,pv_id):
    try:
        pv = PV.objects.get(pk=pv_id)
    except PV.DoesNotExist:
        return redirect('accident:detail_saisine')
    form = PVForm(request.POST or None, instance=pv)
    if form.is_valid():
        form.save()
        return redirect('accident:saisine')
    context = {
        'form': form,
    }
    return render(request, 'pv/saisine/enregistrement.html',context)
@login_required(login_url='login:accident')
@allowed_user(allowed_roles=['accident','secretariat'])
def delete(request,pv_id):
    pv = PV.objects.get(pk=pv_id)
    pv.delete()
    return redirect('accident:saisine')
"""Fin Saisine"""
