from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from authentification.models import Agent
from postepolice.forms import PlainteForm, PerteForm, EcrouForm, ObjectConsigneForm, MainCouranteForm, RegistreForm
from postepolice.models import Plainte, Perte, Ecrou, ObjectConsigne, MainCourante, Brigade, AgentPoste, Registre


def plainte(request):
    listPlainte = Plainte.objects.all
    context = {
        'listPlainte': listPlainte
    }
    return render(request, 'plainte/plainte.html',context);
def detailPlainte(request, id):
    try:
        plainte = Plainte.objects.get(pk=id)
    except Plainte.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'plainte/detail_plainte.html', {'plainte': plainte})
def savePlainte(request,id):
    registre = Registre.objects.get(pk=id)
    if request.method == 'POST':
        form = PlainteForm(request.POST)
        if form.is_valid():
            plainte=form.save(commit=False)
            plainte.registre = registre
            plainte.save()
            return redirect('poste:detail_registre_Pl',id=registre.id)
    else:
        form = PlainteForm
    return render(request, 'plainte/enregistrement.html',{'form':form})
def updatePlainte(request,id):
    try:
        plainte = Plainte.objects.get(pk=id)
    except Plainte.DoesNotExist:
        return redirect('poste:detail_plainte')
    form = PlainteForm(request.POST or None, instance=plainte)
    if form.is_valid():
        form.save()
        return redirect('poste:plainte')
    context = {
        'form': form,
    }
    return render(request, 'plainte/enregistrement.html',context)
def deletePlainte(id):
    plainte = Plainte.objects.get(pk=id)
    plainte.delete()
    return redirect('poste:plainte')





def perte(request):
    listPerte = Perte.objects.all
    context = {
        'listPerte': listPerte
    }
    return render(request, 'perte/perte.html',context);
def detailPerte(request, id):
    try:
        pv = Perte.objects.get(pk=id)
    except Perte.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'perte/detail_perte.html', {'perte': perte})
def savePerte(request,id):
    registre = Registre.objects.get(pk=id)
    if request.method == 'POST':
        form = PerteForm(request.POST)
        if form.is_valid():
            perte=form.save(commit=False)
            perte.registre = registre
            perte.save()
            return redirect('poste:detail_registre_Per',id=registre.id)
    else:
        form = PerteForm
    return render(request, 'perte/enregistrement.html',{'form':form})
def updatePerte(request,id):
    try:
        perte =Perte.objects.get(pk=id)
    except Perte.DoesNotExist:
        return redirect('poste:detail_perte')
    form = PerteForm(request.POST or None, instance=perte)
    if form.is_valid():
        form.save()
        return redirect('poste:perte')
    context = {
        'form': form,
    }
    return render(request, 'perte/enregistrement.html',context)
def deletePerte(id):
    perte = Perte.objects.get(pk=id)
    perte.delete()
    return redirect('poste:perte')




def ecrou(request):
    listEcrou = Ecrou.objects.all
    context = {
        'listEcrou': listEcrou
    }
    return render(request, 'ecrou/ecrou.html',context);
def detailEcrou(request,id):
    try:
        ecrou=Ecrou.objects.get(pk=id)
    except Ecrou.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'ecrou/detail_ecrou.html', {'ecrou':ecrou})
def saveEcrou(request,id):
    registre = Registre.objects.get(pk=id)
    if request.method == 'POST':
        form = EcrouForm(request.POST)
        if form.is_valid():
            ecrou=form.save(commit=False)
            ecrou.registre=registre
            ecrou.save()
            return redirect('poste:detail_registre_Ec',id=registre.id)
    else:
        form = EcrouForm
    return render(request, 'ecrou/enregistrement.html',{'form':form})
def updateEcrou(request,id):
    try:
        ecrou=Ecrou.objects.get(pk=id)
    except Ecrou.DoesNotExist:
        return redirect('poste:detail_ecrou')
    form = EcrouForm(request.POST or None, instance=ecrou)
    if form.is_valid():
        form.save()
        return redirect('poste:ecrou')
    context = {
        'form': form,
    }
    return render(request, 'ecrou/enregistrement.html',context)
def deleteEcrou(id):
    ecrou =Ecrou.objects.get(pk=id)
    ecrou.delete()
    return redirect('poste:ecrou')




def objetConsigne(request):
    listObjectConsigne = ObjectConsigne.objects.all
    context = {
        'listObjectConsigne': listObjectConsigne
    }
    return render(request, 'consigne/consigne.html',context);
def detailObjetConsigne(request, id):
    try:
        objetConsigne=ObjectConsigne.objects.get(pk=id)
    except ObjectConsigne.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'consigne/detail_consigne.html', {'objetConsigne': objetConsigne})
def saveObjetConsigne(request):
    if request.method == 'POST':
        form = ObjectConsigneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poste:objet_consigne')
    else:
        form = ObjectConsigneForm
    return render(request, 'consigne/enregistrement.html',{'form':form})
def updateObjetConsigne(request,id):
    try:
        objetConsigne=ObjectConsigne.objects.get(pk=id)
    except ObjectConsigne.DoesNotExist:
        return redirect('poste:detail_objet_consigne')
    form = ObjectConsigneForm(request.POST or None, instance=objetConsigne)
    if form.is_valid():
        form.save()
        return redirect('poste:objet_consigne')
    context = {
        'form': form,
    }
    return render(request, 'consigne/enregistrement.html',context)
def deleteObjetConsigne(id):
    objetConsigne=ObjectConsigne.objects.get(pk=id)
    objetConsigne.delete()
    return redirect('poste:objet_consigne')




def mainCourante(request):
    listMainCourante = MainCourante.objects.all
    context = {
        'listMainCourante': listMainCourante
    }
    return render(request, 'courante/courante.html',context);
def detailMainCourante(request, id):
    try:
        mainCourante =MainCourante.objects.get(pk=id)
    except MainCourante.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'courante/detail_courante.html', {'mainCourante': mainCourante})
def saveMainCourante(request,id):
    registre = Registre.objects.get(pk=id)
    if request.method == 'POST':
        form = MainCouranteForm(request.POST)
        if form.is_valid():
            courante = form.save(commit=False)
            courante.registre = registre
            courante.save()
            return redirect('poste:detail_registre_MC',id=registre.id)
    else:
        form = MainCouranteForm
    return render(request, 'courante/enregistrement.html',{'form':form})
def updateMainCourante(request,id):
    try:
        mainCourante=MainCourante.objects.get(pk=id)
    except MainCourante.DoesNotExist:
        return redirect('poste:detail_main_courante')
    form = MainCouranteForm(request.POST or None, instance=mainCourante)
    if form.is_valid():
        form.save()
        return redirect('poste:main_courante')
    context = {
        'form': form,
    }
    return render(request, 'courante/enregistrement.html',context)
def deleteMainCourante(id):
    mainCourante=MainCourante.objects.get(pk=id)
    mainCourante.delete()
    return redirect('poste:main_courante')

def listRegistreMC(request):
    listRegistre = Registre.objects.filter(nom="Main Courante")
    context = {
        'listRegistre' : listRegistre,
    }
    return render(request, 'courante/courante.html',context)
def listRegistrePl(request):
    listRegistre = Registre.objects.filter(nom="Plainte")
    context = {
        'listRegistre' : listRegistre,
    }
    return render(request, 'plainte/plainte.html',context)
def listRegistreEc(request):
    listRegistre = Registre.objects.filter(nom="Ecrou")
    context = {
        'listRegistre' : listRegistre,
    }
    return render(request, 'ecrou/ecrou.html',context)
def listRegistrePer(request):
    listRegistre = Registre.objects.filter(nom="Perte")
    context = {
        'listRegistre' : listRegistre,
    }
    return render(request, 'perte/perte.html',context)

def detailRegistreMC(request,id):
    registre = Registre.objects.get(pk=id)
    listMainCourante = MainCourante.objects.filter(registre=registre)
    context = {
        'registre':registre,
        'listMainCourante':listMainCourante
    }
    return render(request, 'courante/detail_courante.html',context)
def detailRegistrePl(request,id):
    registre = Registre.objects.get(pk=id)
    listPlainte = Plainte.objects.filter(registre=registre)
    context = {
        'registre':registre,
        'listPlainte':listPlainte
    }
    return render(request, 'plainte/detail_plainte.html',context)
def detailRegistrePer(request,id):
    registre = Registre.objects.get(pk=id)
    listPerte = Perte.objects.filter(registre=registre)
    context = {
        'registre':registre,
        'listPerte':listPerte
    }
    return render(request, 'perte/detail_perte.html',context)
def detailRegistreEc(request,id):
    registre = Registre.objects.get(pk=id)
    listEcrou = Ecrou.objects.filter(registre=registre)
    context = {
        'registre':registre,
        'listEcrou':listEcrou
    }
    return render(request, 'ecrou/detail_ecrou.html',context)


def saveRegistreMC(request):
    if request.method == 'POST':
        form = RegistreForm(request.POST)
        if form.is_valid():
            registre=form.save(commit=False)
            registre.nom ="Main Courante"
            registre.save()
            registre = Registre.objects.last()
            return redirect('poste:detail_registre_MC',id =registre.id)
    else:
        form = RegistreForm
    return render(request, 'courante/enregistrement.html',{'form':form})
def saveRegistrePl(request):
    if request.method == 'POST':
        form = RegistreForm(request.POST)
        if form.is_valid():
            registre = form.save(commit=False)
            registre.nom = "Plainte"
            registre.save()
            registre = Registre.objects.last()
            return redirect('poste:detail_registre_Pl', id=registre.id)
    else:
        form = RegistreForm
    return render(request, 'plainte/enregistrement.html',{'form':form})
def saveRegistreEc(request):
    if request.method == 'POST':
        form = RegistreForm(request.POST)
        if form.is_valid():
            registre = form.save(commit=False)
            registre.nom = "Ecrou"
            registre.save()
            registre = Registre.objects.last()
            return redirect('poste:detail_registre_Ec', id=registre.id)
    else:
        form = RegistreForm
    return render(request, 'ecrou/enregistrement.html',{'form':form})
def saveRegistrePer(request):
    if request.method == 'POST':
        form = RegistreForm(request.POST)
        if form.is_valid():
            registre = form.save(commit=False)
            registre.nom = "Perte"
            registre.save()
            registre = Registre.objects.last()
            return redirect('poste:detail_registre_Per', id=registre.id)
    else:
        form = RegistreForm
    return render(request, 'perte/enregistrement.html',{'form':form})
