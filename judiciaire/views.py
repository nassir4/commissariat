import socket

from django.http import Http404
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from num2words import num2words
from deep_translator import GoogleTranslator
from judiciaire.models import *
from django.shortcuts import render, redirect
from judiciaire.forms import SaisineForm, InterrogatoireForm, AuditionForm, ClotureForm, ConfrontationForm, \
    MissionForm, RequisitionForm, ConduiteForm, NotificationForm, CrimeForm
from django.http import HttpResponse

# Create your views here.
from judiciaire.utils import render_to_pdf, link_callback


def index (request):
    return render(request,'index.html')
"""Saisine"""
def saisine(request):
    listSaisine = Saisine.objects.all
    context = {
        'listSaisine': listSaisine
    }
    return render(request, 'saisine/saisine.html',context);
def detailSaisine(request, pv_id):
    try:
        pv = Saisine.objects.get(pk=pv_id)
    except Saisine.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'saisine/detail_saisine.html', {'pv': pv})

def save(request,id):
    crime = Crime.objects.get(pk=id)
    if request.method == 'POST':
        form = SaisineForm(request.POST)
        if form.is_valid():
            pv=form.save(commit=False)
            pv.crime=crime
            pv.save()
            return redirect('judiciaire:detail_crime',id=crime.id)
    else:
        form = SaisineForm
    return render(request, 'saisine/enregistrement.html',{'form':form})
def update(request,pv_id):
    try:
        pv = Saisine.objects.get(pk=pv_id)
    except Saisine.DoesNotExist:
        return redirect('judiciaire:detail_saisine')
    form = SaisineForm(request.POST or None, instance=pv)
    if form.is_valid():
        form.save()
        return redirect('judiciaire:detail_saisine',pv_id=pv.id)
    context = {
        'form': form,
    }
    return render(request, 'saisine/enregistrement.html',context)
def delete(request,pv_id):
    pv = Saisine.objects.get(pk=pv_id)
    pv.delete()
    listSaisine = Saisine.objects.all
    return redirect('judiciaire:saisine')

def render_pdf_view(request,id):
    saisine=Saisine.objects.get(pk=id)
    print(num2words(42, lang='fr'))
    year = saisine.dateCreation.strftime("%Y")
    annee =num2words(year, lang='fr')
    day =saisine.dateCreation.strftime("%d")
    jour = num2words(day, lang='fr')
    month = saisine.dateCreation.strftime("%B")
    mois = GoogleTranslator(source='auto', target='fr').translate(month)
    template_path = 'saisine/saisinePDF.html'
    context = {'pv':saisine,'annee':annee,'jour':jour,'mois':mois}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
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

def genererPdf(request,id, *args, **kwargs):
    socket.getaddrinfo('localhost', 8080)
    saisine = Saisine.objects.get(pk=id)
    context = {'pv':saisine}
    pdf = render_to_pdf('saisine/saisinePDF.html', context)
    return HttpResponse(pdf, content_type='application/pdf')
"""Fin Saisine"""
"""Audition"""
def audition(request):
    listAudition = Audition.objects.all
    context = {
        'listAudition': listAudition
    }
    return render(request, 'audition/audition.html',context);
def detailAudition(request, pv_id):
    try:
        pv = Audition.objects.get(pk=pv_id)
    except Audition.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'audition/detail_audition.html', {'pv': pv})
def saveAudition(request,id):
    crime = Crime.objects.get(pk=id)
    if request.method == 'POST':
        form = AuditionForm(request.POST)
        if form.is_valid():
            pv = form.save(commit=False)
            pv.crime = crime
            pv.save()
            return redirect('judiciaire:detail_crime', id=crime.id)
    else:
        form = AuditionForm
    return render(request, 'audition/enregistrement.html',{'form':form})
def updateAudition(request,pv_id):
    try:
        pv = Audition.objects.get(pk=pv_id)
    except Audition.DoesNotExist:
        return redirect('judiciaire:detail_audition')
    form = AuditionForm(request.POST or None, instance=pv)
    if form.is_valid():
        form.save()
        return redirect('judiciaire:detail_audition',pv_id=pv.id)
    context = {
        'form': form,
    }
    return render(request, 'audition/enregistrement.html',context)
def deleteAudition(request,pv_id):
    pv = Audition.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:audition')

"""Fin Audition"""
"""Interrogatoire"""
def interrogatoire(request):
    listInterrogatoire = Interrogatoire.objects.all
    context = {
        'listInterrogatoire': listInterrogatoire
    }
    return render(request, 'interrogatoire/interrogatoire.html',context);
def detailInterrogatoire(request, pv_id):
    try:
        pv = Interrogatoire.objects.get(pk=pv_id)
    except Interrogatoire.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'interrogatoire/detail_interrogatoire.html', {'pv': pv})
def saveInterrogatoire(request,id):
    crime = Crime.objects.get(pk=id)
    if request.method == 'POST':
        form = InterrogatoireForm(request.POST)
        if form.is_valid():
            pv = form.save(commit=False)
            pv.crime = crime
            pv.save()
            return redirect('judiciaire:detail_crime', id=crime.id)
    else:
        form = InterrogatoireForm
    return render(request, 'interrogatoire/enregistrement.html',{'form':form})
def updateInterrogatoire(request,pv_id):
    try:
        pv = Interrogatoire.objects.get(pk=pv_id)
    except Interrogatoire.DoesNotExist:
        return redirect('judiciaire:detail_interrogatoire')
    form = InterrogatoireForm(request.POST or None, instance=pv)
    if form.is_valid():
        form.save()
        return redirect('judiciaire:detail_interrogatoire',pv_id=pv.id)
    context = {
        'form': form,
    }
    return render(request, 'interrogatoire/enregistrement.html',context)
def deleteInterrogatoire(request,pv_id):
    pv = Interrogatoire.objects.get(pk=pv_id)
    pv.delete()
    listSaisine = Saisine.objects.all
    return redirect('judiciaire:interrogatoire')
"""Confrontation"""
def confrontation(request):
    listConfrontation = Confrontation.objects.all
    context = {
        'listConfrontation': listConfrontation
    }
    return render(request, 'confrontation/confrontation.html',context);
def detailConfrontation(request, pv_id):
    try:
        pv = Confrontation.objects.get(pk=pv_id)
    except Confrontation.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'confrontation/detail_confrontation.html', {'pv': pv})
def saveConfrontation(request,id):
    crime = Crime.objects.get(pk=id)
    if request.method == 'POST':
        form = ConfrontationForm(request.POST)
        if form.is_valid():
            pv = form.save(commit=False)
            pv.crime = crime
            pv.save()
            return redirect('judiciaire:detail_crime', id=crime.id)
        else:
            form = ConfrontationForm
    return render(request, 'confrontation/enregistrement.html',{'form':form})
def updateConfrontation(request,pv_id):
    try:
        pv = Confrontation.objects.get(pk=pv_id)
    except Confrontation.DoesNotExist:
        return redirect('judiciaire:detail_confrontation')
    form = ConfrontationForm(request.POST or None, instance=pv)
    if form.is_valid():
        form.save()
        return redirect('judiciaire:detail_confrontation',pv_id=pv.id)
    context = {
        'form': form,
    }
    return render(request, 'confrontation/enregistrement.html',context)
def deleteConfrontation(request,pv_id):
    pv = Confrontation.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:confrontation')

"""Fin Confrontation"""
"""Mission"""
def mission(request):
    listMission = Mission.objects.all
    context = {
        'listMission': listMission
    }
    return render(request, 'mission/mission.html',context);
def detailMission(request, pv_id):
    try:
        pv = Mission.objects.get(pk=pv_id)
    except Interrogatoire.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'mission/detail_mission.html', {'pv': pv})
def saveMission(request,id):
    crime = Crime.objects.get(pk=id)
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            pv = form.save(commit=False)
            pv.crime = crime
            pv.save()
            return redirect('judiciaire:detail_crime', id=crime.id)
    else:
        form = MissionForm
    return render(request, 'mission/enregistrement.html',{'form':form})
def updateMission(request,pv_id):
    try:
        pv = Mission.objects.get(pk=pv_id)
    except Mission.DoesNotExist:
        return redirect('judiciaire:detail_mission')
    form = MissionForm(request.POST or None, instance=pv)
    if form.is_valid():
        form.save()
        return redirect('judiciaire:detail_mission',pv_id=pv.id)
    context = {
        'form': form,
    }
    return render(request, 'mission/enregistrement.html',context)
def deleteMission(request,pv_id):
    pv = Mission.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:mission')
"""Fin Mission"""
"""Requisition"""
def requisition(request):
    listRequisition = Requisition.objects.all
    context = {
        'listRequisition': listRequisition
    }
    return render(request, 'requisition/requisition.html',context);
def detailRequisition(request, pv_id):
    try:
        pv = Requisition.objects.get(pk=pv_id)
    except Requisition.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'requisition/detail_requisition.html', {'pv': pv})
def saveRequisition(request,id):
    crime = Crime.objects.get(pk=id)
    if request.method == 'POST':
        form = RequisitionForm(request.POST)
        if form.is_valid():
            pv = form.save(commit=False)
            pv.crime = crime
            pv.save()
            return redirect('judiciaire:detail_crime', id=crime.id)
    else:
        form = RequisitionForm
    return render(request, 'requisition/enregistrement.html',{'form':form})
def updateRequisition(request,pv_id):
    try:
        pv = Requisition.objects.get(pk=pv_id)
    except Requisition.DoesNotExist:
        return redirect('judiciaire:detail_requisition')
    form = RequisitionForm(request.POST or None, instance=pv)
    if form.is_valid():
        form.save()
        return redirect('judiciaire:detail_requisition',pv_id=pv.id)
    context = {
        'form': form,
    }
    return render(request, 'requisition/enregistrement.html',context)
def deleteRequisition(request,pv_id):
    pv = Requisition.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:requisition')
"""Fin Requisition"""
"""Conduite"""
def conduite(request):
    listConduite = Conduite.objects.all
    context = {
        'listConduite': listConduite
    }
    return render(request, 'conduite/conduite.html',context);
def detailConduite(request, pv_id):
    try:
        pv = Conduite.objects.get(pk=pv_id)
    except Conduite.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'conduite/detail_conduite.html', {'pv': pv})
def saveConduite(request,id):
    crime = Crime.objects.get(pk=id)
    if request.method == 'POST':
        form = ConduiteForm(request.POST)
        if form.is_valid():
            pv = form.save(commit=False)
            pv.crime = crime
            pv.save()
            return redirect('judiciaire:detail_crime', id=crime.id)
    else:
        form = ConduiteForm
    return render(request, 'conduite/enregistrement.html',{'form':form})
def updateConduite(request,pv_id):
    try:
        pv = Conduite.objects.get(pk=pv_id)
    except Conduite.DoesNotExist:
        return redirect('judiciaire:detail_conduite')
    form = ConduiteForm(request.POST or None, instance=pv)
    if form.is_valid():
        form.save()
        return redirect('judiciaire:detail_conduite',pv_id=pv.id)
    context = {
        'form': form,
    }
    return render(request, 'conduite/enregistrement.html',context)
def deleteConduite(request,pv_id):
    pv = Conduite.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:conduite')

"""Fin Conduite"""
"""Cloture"""
def cloture(request):
    listCloture = Cloture.objects.all
    context = {
        'listCloture': listCloture
    }
    return render(request, 'cloture/cloture.html',context);
def detailCloture(request, pv_id):
    try:
        pv = Cloture.objects.get(pk=pv_id)
    except Cloture.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'cloture/detail_cloture.html', {'pv': pv})
def saveCloture(request,id):
    crime = Crime.objects.get(pk=id)
    if request.method == 'POST':
        form = ClotureForm(request.POST)
        if form.is_valid():
            pv = form.save(commit=False)
            pv.crime = crime
            pv.save()
            return redirect('judiciaire:detail_crime', id=crime.id)
    else:
        form = ClotureForm
    return render(request, 'cloture/enregistrement.html',{'form':form})
def updateCloture(request,pv_id):
    try:
        pv = Cloture.objects.get(pk=pv_id)
    except Cloture.DoesNotExist:
        return redirect('judiciaire:detail_cloture')
    form = ClotureForm(request.POST or None, instance=pv)
    if form.is_valid():
        form.save()
        return redirect('judiciaire:detail_cloture',pv_id=pv.id)
    context = {
        'form': form,
    }
    return render(request, 'cloture/enregistrement.html',context)
def deleteCloture(request,pv_id):
    pv = Cloture.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:cloture')

"""Fin Cloture"""
"""Notifification à Garde à vue"""
def notification(request):
    listNotification = Notification.objects.all
    context = {
        'listNotification': listNotification
    }
    return render(request, 'notification/notification.html',context);
def detailNotification(request, pv_id):
    try:
        pv = Notification.objects.get(pk=pv_id)
    except Notification.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'notification/detail_notification.html', {'pv': pv})
def saveNotification(request,id):
    crime = Crime.objects.get(pk=id)
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            pv = form.save(commit=False)
            pv.crime = crime
            pv.save()
            return redirect('judiciaire:detail_crime', id=crime.id)
    else:
        form = NotificationForm
    return render(request, 'notification/enregistrement.html',{'form':form})
def updateNotification(request,pv_id):
    try:
        pv = Notification.objects.get(pk=pv_id)
    except Notification.DoesNotExist:
        return redirect('judiciaire:detail_notification')
    form = NotificationForm(request.POST or None, instance=pv)
    if form.is_valid():
        form.save()
        return redirect('judiciaire:detail_notification',pv_id=pv.id)
    context = {
        'form': form,
    }
    return render(request, 'notification/enregistrement.html',context)
def deleteNotification(request,pv_id):
    pv = Notification.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:notification')

""" Fin Notifification à Garde à vue"""


def crime(request):
    listCrime = Crime.objects.all
    context = {
        'listCrime': listCrime
    }
    return render(request, 'enquete.html',context);
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
    except Notification.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail_enquete.html', context)
def saveCrime(request):
    if request.method == 'POST':
        form = CrimeForm(request.POST)
        if form.is_valid():
            form.save()
            crime = Crime.objects.last()
            return redirect('judiciaire:detail_crime',id =crime.id)
    else:
        form = CrimeForm
    return render(request, 'enregistrement.html',{'form':form})
def updateCrime(request,id):
    try:
        crime = Crime.objects.get(pk=id)
    except Crime.DoesNotExist:
        return redirect('judiciaire:detail_crime')
    form = NotificationForm(request.POST or None, instance=crime)
    if form.is_valid():
        form.save()
        return redirect('judiciaire:detail_crime',id=crime.id)
    context = {
        'form': form,
    }
    return render(request, 'enregistrement.html',context)
def deleteCrime(id):
    crime = Crime.objects.get(pk=id)
    crime.delete()
    return redirect('judiciaire:crime')
