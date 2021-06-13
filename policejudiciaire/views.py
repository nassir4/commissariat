from django.forms.forms import Form
from django.http import Http404

from policejudiciaire.models import *
from django.shortcuts import render, redirect
from policejudiciaire.forms import SaisineForm, InterrogatoireForm, AuditionForm, ClotureForm, ConfrontationForm, \
    MissionForm, RequisitionForm, ConduiteForm, NotificationForm
from django.db import transaction
# Create your views here.
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
    except PV.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'saisine/detail_saisine.html', {'pv': pv})

def save(request):
    form = SaisineForm
    if request.method == 'POST':
        form = SaisineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('judiciaire:saisine')
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
        return redirect('judiciaire:saisine')
    context = {
        'form': form,
    }
    return render(request, 'saisine/enregistrement.html',context)
def delete(request,pv_id):
    pv = Saisine.objects.get(pk=pv_id)
    pv.delete()
    listSaisine = Saisine.objects.all
    return redirect('judiciaire:saisine')
"""Fin Saisine"""
"""Audition"""
def audition(request):
    listAudition = Audition.objects.all
    context = {
        'listAudition': listAudition
    }
    return render(request, 'plainte/plainte.html',context);
def detailAudition(request, pv_id):
    try:
        pv = Audition.objects.get(pk=pv_id)
    except PV.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'plainte/detail_plainte.html', {'pv': pv})
def saveAudition(request):
    form = AuditionForm
    if request.method == 'POST':
        form = AuditionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('judiciaire:plainte')
    else:
        form = AuditionForm
    return render(request, 'plainte/enregistrement.html',{'form':form})
def updateAudition(request,pv_id):
    try:
        pv = Audition.objects.get(pk=pv_id)
    except Audition.DoesNotExist:
        return redirect('judiciaire:detail_audition')
    form = AuditionForm(request.POST or None, instance=pv)
    if form.is_valid():
        form.save()
        return redirect('judiciaire:plainte')
    context = {
        'form': form,
    }
    return render(request, 'plainte/enregistrement.html',context)
def deleteAudition(request,pv_id):
    pv = Audition.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:plainte')

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
    except PV.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'interrogatoire/detail_interrogatoire.html', {'pv': pv})
def saveInterrogatoire(request):
    form = InterrogatoireForm
    if request.method == 'POST':
        form = InterrogatoireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('judiciaire:interrogatoire')
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
        return redirect('judiciaire:interrogatoire')
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
def saveConfrontation(request):
    form = ConfrontationForm
    if request.method == 'POST':
        form = ConfrontationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('judiciaire:confrontation')
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
        return redirect('judiciaire:confrontation')
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
    except PV.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'mission/detail_mission.html', {'pv': pv})
def saveMission(request):
    form = MissionForm
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('judiciaire:mission')
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
        return redirect('judiciaire:mission')
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
        pv = PV.objects.get(pk=pv_id)
    except PV.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'requisition/detail_requisition.html', {'pv': pv})
def saveRequisition(request):
    form = RequisitionForm
    if request.method == 'POST':
        form = RequisitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('judiciaire:requisition')
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
        return redirect('judiciaire:requisition')
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
    except PV.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'conduite/detail_conduite.html', {'pv': pv})
def saveConduite(request):
    form = ConduiteForm
    if request.method == 'POST':
        form = ConduiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('judiciaire:conduite')
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
        return redirect('judiciaire:conduite')
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
    except PV.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'cloture/detail_cloture.html', {'pv': pv})
def saveCloture(request):
    form = ClotureForm
    if request.method == 'POST':
        form = ClotureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('judiciaire:cloture')
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
        return redirect('judiciaire:cloture')
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
    except PV.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'notification/detail_notification.html', {'pv': pv})
def saveNotification(request):
    form = NotificationForm
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('judiciaire:notification')
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
        return redirect('judiciaire:notification')
    context = {
        'form': form,
    }
    return render(request, 'notification/enregistrement.html',context)
def deleteNotification(request,pv_id):
    pv = Notification.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:notification')

""" Fin Notifification à Garde à vue"""

def listPv(request):
    listPV =PV.objects.all
    return render(request,'accueil.html',{'listPV':listPV})