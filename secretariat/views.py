from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from accident.models import Accident
from authentification.decorators import allowed_user
from pojudiciaire.models import Crime
from postepolice.forms import RegistreForm
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
    return render(request, 'poste/plainte/detail_plainte.html',context)
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
