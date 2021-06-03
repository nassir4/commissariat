from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from accident.forms import TypeAccidentForm, AccidentForm, VehiculeForm, EclairageForm, EssuieGlaceForm, \
    RetroviseurForm, IndicateurVitesseForm, IndicateurDirectionForm, AvertisseurForm, ConducteurForm, VictimeForm, \
    TemoinForm, EtatDesLieuxForm, DeclarationForm
from accident.models import TypeAccident, Accident, EssuieGlace


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

def saveAccident(request):
    form = AccidentForm
    if request.method == 'POST':
        form =AccidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accident:accident')
    else:
        form = AccidentForm
    return render(request, 'enregistrement_accident.html',{'form':form})
def updateAccident(request,type_id):
    try:
        accident = Accident.objects.get(pk=type_id)
    except Accident.DoesNotExist:
        return redirect('accident:detail_accident')
    form = AccidentForm(request.POST or None, instance=typeAccident)
    if form.is_valid():
        form.save()
        return redirect('accident:accident')
    context = {
        'form': form,
    }
    return render(request, 'enregistrement_accident.html',context)
def deleteAccident(request,type_id):
    accident = Accident.objects.get(pk=type_id)
    accident.delete()
    return redirect('accident:accident')
### Fin Accident ####
### Vehicule
def saveVehicule(request):
    form = VehiculeForm
    if request.method == 'POST':
        form =VehiculeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accident:vehicule')
    else:
        form = VehiculeForm
    return render(request, 'enregistrement_vehicule.html',{'form':form})
### Fin vehicule
def saveAccessoire(request):
    if request.method == 'POST':
        form_eclairage =EclairageForm(request.POST)
        if form_eclairage.is_valid():
            form_eclairage.save()
            return redirect('accident:vehicule')
        form_essuie_glace = EssuieGlaceForm(request.POST)
        if form_essuie_glace.is_valid():
            form_essuie_glace.save()
            return redirect('accident:vehicule')
        form_retroviseur = RetroviseurForm(request.POST)
        if form_retroviseur.is_valid():
            form_retroviseur.save()
            return redirect('accident:vehicule')
        form_vitesse = IndicateurVitesseForm(request.POST)
        if form_vitesse.is_valid():
            form_vitesse.save()
            return redirect('accident:vehicule')
        form_direction = IndicateurDirectionForm(request.POST)
        if form_direction.is_valid():
            form_direction.save()
            return redirect('accident:vehicule')
        form_avertisseur = AvertisseurForm(request.POST)
        if form_avertisseur.is_valid():
            form_avertisseur.save()
            return redirect('accident:vehicule')
    else:
        form_eclairage = EclairageForm
        form_essuie_glace = EssuieGlaceForm
        form_retroviseur = RetroviseurForm
        form_vitesse = IndicateurVitesseForm
        form_direction = IndicateurDirectionForm
        form_avertisseur = AvertisseurForm
    return render(request, 'enregistrement_accessoire.html',{
        'form_eclairage':form_eclairage,
        'form_essuie_glace':form_essuie_glace,
        'form_retroviseur':form_retroviseur,
        'form_vitesse':form_vitesse,
        'form_direction':form_direction,
        'form_avertisseur':form_avertisseur,
    })
##Fin Accessoires
## Conducteur
def saveConducteur(request):
    if request.method == 'POST':
        form = ConducteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accident:conducteur')
    else:
        form = ConducteurForm
    return render(request, 'enregistrement_conducteur.html', {'form': form})
## Fin Conducteur
## Victime
def saveVictime(request):
    if request.method == 'POST':
        form = VictimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accident:conducteur')
    else:
        form = VictimeForm
    return render(request, 'enregistrement_victime.html', {'form': form})
#Fin Victime
# Temoin
def saveTemoin(request):
    if request.method == 'POST':
        form =TemoinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accident:conducteur')
    else:
        form = TemoinForm
    return render(request, 'enregistrement_temoin.html', {'form': form})
# Etat des lieux
def saveEtat(request):
    if request.method == 'POST':
        form =EtatDesLieuxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accident:conducteur')
    else:
        form = EtatDesLieuxForm
    return render(request, 'enregistrement_etat.html', {'form': form})
# Conducteur
def saveDeclaration(request):
    if request.method == 'POST':
        form =DeclarationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accident:conducteur')
    else:
        form = DeclarationForm
    return render(request, 'enregistrement_declaration.html', {'form': form})
