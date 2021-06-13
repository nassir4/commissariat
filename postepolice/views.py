from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from postepolice.forms import PlainteForm, PerteForm, EcrouForm, ObjectConsigneForm, MainCouranteForm
from postepolice.models import Plainte, Perte, Ecrou, ObjectConsigne, MainCourante


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
def savePlainte(request):
    if request.method == 'POST':
        form = PlainteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poste:plainte')
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
def savePerte(request):
    if request.method == 'POST':
        form = PerteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poste:perte')
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
def saveEcrou(request):
    if request.method == 'POST':
        form = EcrouForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poste:ecrou')
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
def saveMainCourante(request):
    if request.method == 'POST':
        form = MainCouranteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poste:main_courante')
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
