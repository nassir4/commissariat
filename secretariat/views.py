from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

import secretariat
from accident.models import Accident
from authentification.decorators import allowed_user
from pojudiciaire.models import Crime, Notification, Cloture, Requisition, Conduite, Mission, Confrontation, \
    Interrogatoire, Audition, Saisine
from postepolice.forms import RegistreForm, PlainteAffecte, MainCouranteAffecte, MainCouranteVue
from postepolice.models import Registre, Plainte, Perte, Ecrou, MainCourante, GardeAVue


@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def index (request):
    listAccidentCorporel =Accident.objects.filter(type_accident=1)
    listAccidentMateriel = Accident.objects.filter(type_accident=2)
    listCrime1 = Crime.objects.filter(typeInfraction=1)
    listCrime2 = Crime.objects.filter(typeInfraction=2)
    listCrime3 = Crime.objects.filter(typeInfraction=3)
    listCrime4 = Crime.objects.filter(typeInfraction=4)
    listCrime5 = Crime.objects.filter(typeInfraction=5)
    listRegistre=Registre.objects.all
    listUser =User.objects.all

    context ={
        'listAccidentCorporel':listAccidentCorporel,
        'listAccidentMateriel':listAccidentMateriel,
        'listCrime1':listCrime1,
        'listCrime2': listCrime2,
        'listCrime3':listCrime3,
        'listCrime4':listCrime4,
        'listCrime5':listCrime5,
        'listUser':listUser,
        'listRegistre':listRegistre
    }
    return render(request,'secretariat.html',context)


class ChartData(APIView):
    authentification=[]
    permission_classes = []

    def get(self,request,format=None):
        materiel =Accident.objects.filter(type_accident=1).count()
        corporel =Accident.objects.filter(type_accident=2).count()
        labels =["Accident Materiel","Accident Corporel"]
        default_items = [materiel,corporel]
        data={
            "labels":labels,
            "default":default_items
        }
        return Response(data)

class ChartPie(APIView):
    authentification=[]
    permission_classes = []

    def get(self,request,format=None):
        c1 = Crime.objects.filter(typeInfraction=1).count()
        c2 = Crime.objects.filter(typeInfraction=2).count()
        c3 = Crime.objects.filter(typeInfraction=3).count()
        c4 = Crime.objects.filter(typeInfraction=4).count()
        c5 = Crime.objects.filter(typeInfraction=5).count()
        labels =["CDCCP","ATAA","CDCP","ILTIC","ILS"]
        default_items = [c1,c2,c3,c4,c5]
        data={
            "labels":labels,
            "default":default_items
        }
        return Response(data)


@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def plainte(request):
    listPlainte = Plainte.objects.all
    context = {
        'listPlainte': listPlainte
    }
    return render(request, 'poste/plainte/plainte.html',context);
@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailPlainte(request, id):
    try:
        plainte = Plainte.objects.get(pk=id)
    except Plainte.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'poste/plainte/detail_plainte.html', {'plainte': plainte})


@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def perte(request):
    listPerte = Perte.objects.all
    context = {
        'listPerte': listPerte
    }
    return render(request, 'poste/perte/perte.html',context);
@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailPerte(request, id):
    try:
        pv = Perte.objects.get(pk=id)
    except Perte.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'poste/perte/detail_perte.html', {'perte': perte})

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def ecrou(request):
    listEcrou = Ecrou.objects.all
    context = {
        'listEcrou': listEcrou
    }
    return render(request, 'poste/ecrou/ecrou.html',context);
@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailEcrou(request,id):
    try:
        ecrou=Ecrou.objects.get(pk=id)
    except Ecrou.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'poste/ecrou/detail_ecrou.html', {'ecrou':ecrou})


@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def mainCourante(request):
    listMainCourante = MainCourante.objects.all
    context = {
        'listMainCourante': listMainCourante
    }
    return render(request, 'poste/courante/courante.html',context);
@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailMainCourante(request, id):
    try:
        mainCourante =MainCourante.objects.get(pk=id)
    except MainCourante.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'poste/courante/detail_courante.html', {'mainCourante': mainCourante})


@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def listRegistreMC(request):
    listRegistre = Registre.objects.filter(nom="Main Courante")
    context = {
        'listRegistre' : listRegistre,
    }
    return render(request, 'poste/courante/courante.html',context)
@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def listRegistrePl(request):
    listRegistre = Registre.objects.filter(nom="Plainte")
    context = {
        'listRegistre' : listRegistre,
    }
    return render(request, 'poste/plainte/plainte.html',context)
@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def listRegistreEc(request):
    listRegistre = Registre.objects.filter(nom="Ecrou")
    context = {
        'listRegistre' : listRegistre,
    }
    return render(request, 'poste/ecrou/ecrou.html',context)
@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def listRegistrePer(request):
    listRegistre = Registre.objects.filter(nom="Perte")
    context = {
        'listRegistre' : listRegistre,
    }
    return render(request, 'poste/perte/perte.html',context)

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def listRegistreGarde(request):
    listRegistre = Registre.objects.filter(nom="Garde à vue")
    context = {
        'listRegistre' : listRegistre,
    }
    return render(request, 'poste/garde/garde_a_vue.html',context)

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailRegistreMC(request,id):
    registre = Registre.objects.get(pk=id)
    listMainCourante = MainCourante.objects.filter(registre=registre)
    context = {
        'registre':registre,
        'listMainCourante':listMainCourante
    }
    return render(request, 'poste/courante/detail_courante.html',context)
@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailRegistreGarde(request,id):
    registre = Registre.objects.get(pk=id)
    listGarde = GardeAVue.objects.filter(registre=registre)
    context = {
        'registre':registre,
        'listGarde':listGarde
    }
    return render(request, 'poste/garde/detail_registre.html',context)

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailRegistrePl(request,id):
    registre = Registre.objects.get(pk=id)
    listPlainte = Plainte.objects.filter(registre=registre)
    context = {
        'registre':registre,
        'listPlainte':listPlainte
    }
    return render(request, 'poste/plainte/detail_registre.html',context)
@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailRegistrePer(request,id):
    registre = Registre.objects.get(pk=id)
    listPerte = Perte.objects.filter(registre=registre)
    context = {
        'registre':registre,
        'listPerte':listPerte
    }
    return render(request, 'poste/perte/detail_perte.html',context)
@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailRegistreEc(request,id):
    registre = Registre.objects.get(pk=id)
    listEcrou = Ecrou.objects.filter(registre=registre)
    context = {
        'registre':registre,
        'listEcrou':listEcrou
    }
    return render(request, 'poste/ecrou/detail_ecrou.html',context)


@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailGardeAVue(request, id):
    try:
        garde =GardeAVue.objects.get(pk=id)
    except GardeAVue.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'poste/garde/detail_garde.html', {'garde': garde})

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def plainteAffecte(request,id):
    try:
        plainte=Plainte.objects.get(pk=id)
    except Plainte.DoesNotExist:
        return redirect('poste:detail_objet_consigne')
    form = PlainteAffecte(request.POST or None, instance=plainte)
    if form.is_valid():
        form.save()
        return redirect('secretariat:detail_registre_Pl', id=plainte.registre.id)
    context = {
        'form': form,
    }
    return render(request, 'poste/plainte/enregistrement.html',context)

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def mainCouranteAffecte(request,id):
    try:
        mainCourante=MainCourante.objects.get(pk=id)
    except MainCourante.DoesNotExist:
        return redirect('poste:detail_objet_consigne')
    form = MainCouranteAffecte(request.POST or None, instance=mainCourante)
    if form.is_valid():
        form.save()
        return redirect('secretariat:detail_registre_MC', id=mainCourante.registre.id)
    context = {
        'form': form,
    }
    return render(request, 'poste/courante/enregistrement.html',context)

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def mainCouranteVue(request,id):
    try:
        mainCourante=MainCourante.objects.get(pk=id)
    except MainCourante.DoesNotExist:
        return redirect('poste:detail_objet_consigne')
    form = MainCouranteVue(request.POST or None, instance=mainCourante)
    if form.is_valid():
        form.save()
        return redirect('secretariat:detail_registre_MC', id=mainCourante.registre.id)
    context = {
        'form': form,
    }
    return render(request, 'poste/courante/enregistrement.html',context)

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def crime(request):
    listCrime = Crime.objects.all
    context = {
        'listCrime': listCrime
    }
    return render(request, 'judiciaire/enquete.html',context);

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailCrime(request, id):
    try:
        crime = Crime.objects.get(pk=id)
        listSaisine = Saisine.objects.filter(crime=crime)
        listAudition = Audition.objects.filter(crime=crime)
        listInterrogatoire = Interrogatoire.objects.filter(crime=crime)
        listConfrontation = Confrontation.objects.filter(crime=crime)
        listMission =Mission.objects.filter(crime=crime)
        listConduite = Conduite.objects.filter(crime=crime)
        listRequisition = Requisition.objects.filter(crime=crime)
        listNotification = Notification.objects.filter(crime=crime)
        listCloture = Cloture.objects.filter(crime=crime)
        context = {
            'crime': crime,
            'listSaisine':listSaisine,
            'listAudition':listAudition,
            'listInterrogatoire':listInterrogatoire,
            'listConfrontation':listConfrontation,
            'listMission':listMission,
            'listConduite': listConduite,
            'listRequisition':listRequisition,
            'listNotification':listNotification,
            'listCloture':listCloture
        }
    except Crime.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'judiciaire/detail_enquete.html', context)

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailSaisine(request, pv_id):
    try:
        pv = Saisine.objects.get(pk=pv_id)
    except Saisine.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'judiciaire/saisine/detail_saisine.html', {'pv': pv})
@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailAudition(request, pv_id):
    try:
        pv = Audition.objects.get(pk=pv_id)
    except Audition.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'judiciaire/audition/detail_audition.html', {'pv': pv})

@login_required(login_url='login:secretaire')
@allowed_user(allowed_roles=['secretariat'])
def detailInterrogatoire(request, pv_id):
    try:
        pv = Interrogatoire.objects.get(pk=pv_id)
    except Interrogatoire.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'judiciaire/interrogatoire/detail_interrogatoire.html', {'pv': pv})

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailConfrontation(request, pv_id):
    try:
        pv = Confrontation.objects.get(pk=pv_id)
    except Confrontation.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'judiciaire/confrontation/detail_confrontation.html', {'pv': pv})

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailMission(request, pv_id):
    try:
        pv = Mission.objects.get(pk=pv_id)
    except Interrogatoire.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'judiciaire/mission/detail_mission.html', {'pv': pv})

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailRequisition(request, pv_id):
    try:
        pv = Requisition.objects.get(pk=pv_id)
    except Requisition.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'judiciaire/requisition/detail_requisition.html', {'pv': pv})

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailConduite(request, pv_id):
    try:
        pv = Conduite.objects.get(pk=pv_id)
    except Conduite.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'judiciaire/conduite/detail_conduite.html', {'pv': pv})

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailCloture(request, pv_id):
    try:
        pv = Cloture.objects.get(pk=pv_id)
    except Cloture.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'judiciaire/cloture/detail_cloture.html', {'pv': pv})
@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def detailNotification(request, pv_id):
    try:
        pv = Notification.objects.get(pk=pv_id)
    except Notification.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'judiciaire/notification/detail_notification.html', {'pv': pv})


