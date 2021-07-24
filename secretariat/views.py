from chartjs.views.lines import BaseLineChartView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from accident.models import Accident
from judiciaire.models import Crime, Incrimination
from postepolice.models import Registre

@login_required(login_url='login:secretariat')
def index (request):
    listAccidentCorporel =Accident.objects.filter(type_accident=1)
    listAccidentMateriel = Accident.objects.filter(type_accident=2)
    listCrime = Crime.objects.all
    listRegistre=Registre.objects.all
    listUser =User.objects.all

    context ={
        'listAccidentCorporel':listAccidentCorporel,
        'listAccidentMateriel':listAccidentMateriel,
        'listCrime':listCrime,
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
        materiel =Accident.objects.filter(type_accident=1).count()
        corporel =Accident.objects.filter(type_accident=2).count()
        labels =["Accident Materiel","Accident Corporel"]
        default_items = [materiel,corporel]
        data={
            "labels":labels,
            "default":default_items
        }
        return Response(data)
