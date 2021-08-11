from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import get_template
from num2words import num2words
from rest_framework.response import Response
from rest_framework.views import APIView
from xhtml2pdf import pisa

import secretariat
from accident.models import Accident, Declaration, Conducteur, Assurance, Permis, Proprietaire, Eclairage, \
    IndicateurDirection, Avertisseur, IndicateurVitesse, EssuieGlace, EtatDesLieux, Victime, Temoin, Vehicule, \
    Retroviseur
from authentification.decorators import allowed_user
from pojudiciaire.models import Crime, Notification, Cloture, Requisition, Conduite, Mission, Confrontation, \
    Interrogatoire, Audition, Saisine
from pojudiciaire.utils import link_callback
from postepolice.forms import RegistreForm, PlainteAffecte, MainCouranteAffecte, MainCouranteVue
from postepolice.models import Registre, Plainte, Perte, Ecrou, MainCourante, GardeAVue
from secretariat.form import GallerieForm, ImagePotForm
from secretariat.models import Gallerie, ImagePot


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


@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def accident(request):
    listaccident = Accident.objects.all
    context = {
        'listAccident': listaccident
    }
    return render(request, 'accident/accident.html',context);

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
    return render(request, 'accident/detail_accident.html', context)

@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def render_pdf_accident(request,id):
    accident=Accident.objects.get(pk=id)
    print(num2words(42, lang='fr'))
    year = accident.date_accident.strftime("%Y")
    annee =num2words(year, lang='fr')
    day =accident.date_accident.strftime("%d")
    jour = num2words(day, lang='fr')
    Mois=['janvier','fevrier','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','Decembre']
    month = int(accident.date_accident.strftime("%m"))
    mois = Mois[month-1]
    hour = accident.date_accident.strftime("%H")
    heure =num2words(hour, lang='fr')
    m=accident.date_accident.strftime("%M")
    print(m)
    minutes = num2words(m, lang='fr')
    template_path = 'accident/accidentPDF.html'
    listVehicule = Vehicule.objects.filter(accident=accident)
    listConducteur = []
    listAssurance = []
    listPermis = []
    listTemoin = Temoin.objects.filter(accident=accident)
    listVictime = Victime.objects.filter(accident=accident)
    etatDesLieux = EtatDesLieux.objects.filter(accident=accident)
    listProprietaire = []
    listEclairage = []
    listDirection = []
    listAvertisseur = []
    listVitesse = []
    listEssuieGlace = []
    listRetroviseur =[]
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
    if accident.type_accident.nom == "Accident Materiel":
        accidentCorporel = False
    if accident.type_accident.nom == "Accident Corporel":
        accidentCorporel = True
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
        for vehicule in listVehicule:
            listRetroviseur.append(Retroviseur.objects.get(vehicule=vehicule))

    context = {
        'accidentCorporel': accidentCorporel,
        'listProprietaire': listProprietaire,
        'listDeclaration': listDeclaration,
        'listTemoin': listTemoin,
        'listVictime': listVictime,
        'listPermis': listPermis,
        'listAssurance': listAssurance,
        'listConducteur': listConducteur,
        'accident': accident,
        'listVehicule': listVehicule,
        'etatDesLieux': etatDesLieux,
        'listVitesse': listVitesse,
        'listDirection': listDirection,
        'listAvertisseur': listAvertisseur,
        'listEclairage': listEclairage,
        'listEssuieGlace': listEssuieGlace,
        'listRetroviseur':listRetroviseur,
        'annee':annee,'jour':jour,
        'mois':mois,
        'heure':heure,
        'minutes':minutes}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Constat.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
@login_required(login_url='login:secretariat')
@allowed_user(allowed_roles=['secretariat'])
def render_pdf_accident2(request,id):
    accident=Accident.objects.get(pk=id)
    print(num2words(42, lang='fr'))
    year = accident.date_accident.strftime("%Y")
    annee =num2words(year, lang='fr')
    day =accident.date_accident.strftime("%d")
    jour = num2words(day, lang='fr')
    Mois=['janvier','fevrier','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','Decembre']
    month = int(accident.date_accident.strftime("%m"))
    mois = Mois[month-1]
    hour = accident.date_accident.strftime("%H")
    heure =num2words(hour, lang='fr')
    m=accident.date_accident.strftime("%M")
    print(m)
    minutes = num2words(m, lang='fr')
    template_path = 'accident/accidentPDF2.html'
    listVehicule = Vehicule.objects.filter(accident=accident)
    listConducteur = []
    listAssurance = []
    listPermis = []
    listTemoin = Temoin.objects.filter(accident=accident)
    listVictime = Victime.objects.filter(accident=accident)
    etatDesLieux = EtatDesLieux.objects.filter(accident=accident)
    listProprietaire = []
    listEclairage = []
    listDirection = []
    listAvertisseur = []
    listVitesse = []
    listEssuieGlace = []
    listRetroviseur =[]
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
    if accident.type_accident.nom == "Accident Materiel":
        accidentCorporel = False
    if accident.type_accident.nom == "Accident Corporel":
        accidentCorporel = True
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
        for vehicule in listVehicule:
            listRetroviseur.append(Retroviseur.objects.get(vehicule=vehicule))

    context = {
        'accidentCorporel': accidentCorporel,
        'listProprietaire': listProprietaire,
        'listDeclaration': listDeclaration,
        'listTemoin': listTemoin,
        'listVictime': listVictime,
        'listPermis': listPermis,
        'listAssurance': listAssurance,
        'listConducteur': listConducteur,
        'accident': accident,
        'listVehicule': listVehicule,
        'etatDesLieux': etatDesLieux,
        'listVitesse': listVitesse,
        'listDirection': listDirection,
        'listAvertisseur': listAvertisseur,
        'listEclairage': listEclairage,
        'listEssuieGlace': listEssuieGlace,
        'listRetroviseur':listRetroviseur,
        'annee':annee,'jour':jour,
        'mois':mois,
        'heure':heure,
        'minutes':minutes}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Constat.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
def saveGallerie(request):
    if request.method == 'POST':
        form = GallerieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            gallerie = Gallerie.objects.last()
            return redirect('secretariat:detail_gallerie',id=gallerie.id)
    else:
        form = GallerieForm
    return render(request, 'enregistrement_gal.html',{'form':form})
def gallerieDetail(request,id):
    gallerie = Gallerie.objects.get(pk=id)
    listImage=ImagePot.objects.filter(gallerie=gallerie)
    if request.method == 'POST':
        form = ImagePotForm(request.POST,request.FILES)
        if form.is_valid():
            imagePot = form.save(commit=False)
            imagePot.gallerie = gallerie
            imagePot.save()
            listImage = ImagePot.objects.filter(gallerie=gallerie).order_by('id').reverse()
    else:
        form = ImagePotForm
    return render(request, 'gallerie_detail.html',{'form':form,'gallerie':gallerie,'listImage':listImage,})
def listGalerie(request):
    listGallerie = Gallerie.objects.all().order_by('id').reverse()
    return render(request, 'gallerie.html',{'listGallerie':listGallerie})