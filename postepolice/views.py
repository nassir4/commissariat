from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from authentification.decorators import allowed_user
from authentification.models import Agent
from postepolice.forms import PlainteForm, PerteForm, EcrouForm, ObjectConsigneForm, MainCouranteForm, RegistreForm
from postepolice.models import Plainte, Perte, Ecrou, ObjectConsigne, MainCourante, Brigade, AgentPoste, Registre

@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def plainte(request):
    listPlainte = Plainte.objects.all
    context = {
        'listPlainte': listPlainte
    }
    return render(request, 'plainte/plainte.html',context);
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def detailPlainte(request, id):
    try:
        plainte = Plainte.objects.get(pk=id)
    except Plainte.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'plainte/detail_plainte.html', {'plainte': plainte})
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
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
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
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
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def deletePlainte(id):
    plainte = Plainte.objects.get(pk=id)
    plainte.delete()
    return redirect('poste:plainte')




@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def perte(request):
    listPerte = Perte.objects.all
    context = {
        'listPerte': listPerte
    }
    return render(request, 'perte/perte.html',context);
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def detailPerte(request, id):
    try:
        pv = Perte.objects.get(pk=id)
    except Perte.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'perte/detail_perte.html', {'perte': perte})
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
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
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
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
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def deletePerte(id):
    perte = Perte.objects.get(pk=id)
    perte.delete()
    return redirect('poste:perte')



@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def ecrou(request):
    listEcrou = Ecrou.objects.all
    context = {
        'listEcrou': listEcrou
    }
    return render(request, 'ecrou/ecrou.html',context);
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def detailEcrou(request,id):
    try:
        ecrou=Ecrou.objects.get(pk=id)
    except Ecrou.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'ecrou/detail_ecrou.html', {'ecrou':ecrou})
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
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
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
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
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def deleteEcrou(id):
    ecrou =Ecrou.objects.get(pk=id)
    ecrou.delete()
    return redirect('poste:ecrou')



@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def objetConsigne(request):
    listObjectConsigne = ObjectConsigne.objects.all
    context = {
        'listObjectConsigne': listObjectConsigne
    }
    return render(request, 'consigne/consigne.html',context);
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def detailObjetConsigne(request, id):
    try:
        objetConsigne=ObjectConsigne.objects.get(pk=id)
    except ObjectConsigne.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'consigne/detail_consigne.html', {'objetConsigne': objetConsigne})
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def saveObjetConsigne(request):
    if request.method == 'POST':
        form = ObjectConsigneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poste:objet_consigne')
    else:
        form = ObjectConsigneForm
    return render(request, 'consigne/enregistrement.html',{'form':form})
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
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
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def deleteObjetConsigne(id):
    objetConsigne=ObjectConsigne.objects.get(pk=id)
    objetConsigne.delete()
    return redirect('poste:objet_consigne')



@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def mainCourante(request):
    listMainCourante = MainCourante.objects.all
    context = {
        'listMainCourante': listMainCourante
    }
    return render(request, 'courante/courante.html',context);
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def detailMainCourante(request, id):
    try:
        mainCourante =MainCourante.objects.get(pk=id)
    except MainCourante.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'courante/detail_courante.html', {'mainCourante': mainCourante})
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
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
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
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
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def deleteMainCourante(id):
    mainCourante=MainCourante.objects.get(pk=id)
    mainCourante.delete()
    return redirect('poste:main_courante')
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def listRegistreMC(request):
    listRegistre = Registre.objects.filter(nom="Main Courante")
    context = {
        'listRegistre' : listRegistre,
    }
    return render(request, 'courante/courante.html',context)
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def listRegistrePl(request):
    listRegistre = Registre.objects.filter(nom="Plainte")
    context = {
        'listRegistre' : listRegistre,
    }
    return render(request, 'plainte/plainte.html',context)
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def listRegistreEc(request):
    listRegistre = Registre.objects.filter(nom="Ecrou")
    context = {
        'listRegistre' : listRegistre,
    }
    return render(request, 'ecrou/ecrou.html',context)
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def listRegistrePer(request):
    listRegistre = Registre.objects.filter(nom="Perte")
    context = {
        'listRegistre' : listRegistre,
    }
    return render(request, 'perte/perte.html',context)
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def detailRegistreMC(request,id):
    registre = Registre.objects.get(pk=id)
    listMainCourante = MainCourante.objects.filter(registre=registre)
    context = {
        'registre':registre,
        'listMainCourante':listMainCourante
    }
    return render(request, 'courante/detail_courante.html',context)
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def detailRegistrePl(request,id):
    registre = Registre.objects.get(pk=id)
    listPlainte = Plainte.objects.filter(registre=registre)
    context = {
        'registre':registre,
        'listPlainte':listPlainte
    }
    return render(request, 'plainte/detail_plainte.html',context)
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def detailRegistrePer(request,id):
    registre = Registre.objects.get(pk=id)
    listPerte = Perte.objects.filter(registre=registre)
    context = {
        'registre':registre,
        'listPerte':listPerte
    }
    return render(request, 'perte/detail_perte.html',context)
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
def detailRegistreEc(request,id):
    registre = Registre.objects.get(pk=id)
    listEcrou = Ecrou.objects.filter(registre=registre)
    context = {
        'registre':registre,
        'listEcrou':listEcrou
    }
    return render(request, 'ecrou/detail_ecrou.html',context)

@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
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
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
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
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
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
@login_required(login_url='login:poste')
@allowed_user(allowed_roles=['poste de police'])
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
