from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from accident.models import Accident
from pojudiciaire.models import Crime
from postepolice.models import Registre

@login_required(login_url='login:secretariat')
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
