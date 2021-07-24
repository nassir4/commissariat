from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.template.loader import get_template
from xhtml2pdf import pisa
from num2words import num2words
from pojudiciaire.models import *
from django.shortcuts import render, redirect
from pojudiciaire.forms import SaisineForm, InterrogatoireForm, AuditionForm, ClotureForm, ConfrontationForm, \
    MissionForm, RequisitionForm, ConduiteForm, NotificationForm, CrimeForm
from django.http import HttpResponse

# Create your views here.
from pojudiciaire.utils import link_callback

@login_required(login_url='login:judiciaire')
def index (request):
    return render(request,'index.html')
"""Saisine"""
@login_required(login_url='login:judiciaire')
def saisine(request):
    listSaisine = Saisine.objects.all
    context = {
        'listSaisine': listSaisine
    }
    return render(request, 'saisine/saisine.html',context);
@login_required(login_url='login:judiciaire')
def detailSaisine(request, pv_id):
    try:
        pv = Saisine.objects.get(pk=pv_id)
    except Saisine.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'saisine/detail_saisine.html', {'pv': pv})
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
def delete(request,pv_id):
    pv = Saisine.objects.get(pk=pv_id)
    pv.delete()
    listSaisine = Saisine.objects.all
    return redirect('judiciaire:saisine')
@login_required(login_url='login:judiciaire')
def render_pdf_saisine(request,id):
    saisine=Saisine.objects.get(pk=id)
    print(num2words(42, lang='fr'))
    year = saisine.dateCreation.strftime("%Y")
    annee =num2words(year, lang='fr')
    day =saisine.dateCreation.strftime("%d")
    jour = num2words(day, lang='fr')
    Mois=['janvier','fevrier','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','Decembre']
    month = int(saisine.dateCreation.strftime("%m"))
    mois = Mois[month-1]
    hour = saisine.dateCreation.strftime("%H")
    heure =num2words(hour, lang='fr')
    m=saisine.dateCreation.strftime("%M")
    print(m)
    minutes = num2words(m, lang='fr')
    template_path = 'saisine/saisinePDF.html'
    context = {'pv':saisine,'annee':annee,'jour':jour,'mois':mois,'heure':heure, 'minutes':minutes}
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

"""Fin Saisine"""
"""Audition"""
@login_required(login_url='login:judiciaire')
def audition(request):
    listAudition = Audition.objects.all
    context = {
        'listAudition': listAudition
    }
    return render(request, 'audition/audition.html',context);
@login_required(login_url='login:judiciaire')
def detailAudition(request, pv_id):
    try:
        pv = Audition.objects.get(pk=pv_id)
    except Audition.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'audition/detail_audition.html', {'pv': pv})
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
def deleteAudition(request,pv_id):
    pv = Audition.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:audition')
@login_required(login_url='login:judiciaire')
def render_pdf_audition(request,id):
    audition=Audition.objects.get(pk=id)
    print(num2words(42, lang='fr'))
    year = audition.dateCreation.strftime("%Y")
    annee =num2words(year, lang='fr')
    day =audition.dateCreation.strftime("%d")
    jour = num2words(day, lang='fr')
    Mois=['janvier','fevrier','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','Decembre']
    month = int(audition.dateCreation.strftime("%m"))
    mois = Mois[month-1]
    hour = audition.dateCreation.strftime("%H")
    heure =num2words(hour, lang='fr')
    m=audition.dateCreation.strftime("%M")
    print(m)
    minutes = num2words(m, lang='fr')
    template_path = 'audition/auditionPDF.html'
    context = {'pv':audition,'annee':annee,'jour':jour,'mois':mois,'heure':heure, 'minutes':minutes}
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

"""Fin Audition"""
"""Interrogatoire"""
@login_required(login_url='login:judiciaire')
def interrogatoire(request):
    listInterrogatoire = Interrogatoire.objects.all
    context = {
        'listInterrogatoire': listInterrogatoire
    }
    return render(request, 'interrogatoire/interrogatoire.html',context);
@login_required(login_url='login:judiciaire')
def detailInterrogatoire(request, pv_id):
    try:
        pv = Interrogatoire.objects.get(pk=pv_id)
    except Interrogatoire.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'interrogatoire/detail_interrogatoire.html', {'pv': pv})
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
def deleteInterrogatoire(request,pv_id):
    pv = Interrogatoire.objects.get(pk=pv_id)
    pv.delete()
    listSaisine = Saisine.objects.all
    return redirect('judiciaire:interrogatoire')
@login_required(login_url='login:judiciaire')
def render_pdf_interrogatoire(request,id):
    interrogatoire=Interrogatoire.objects.get(pk=id)
    print(num2words(42, lang='fr'))
    year = interrogatoire.dateCreation.strftime("%Y")
    annee =num2words(year, lang='fr')
    day =interrogatoire.dateCreation.strftime("%d")
    jour = num2words(day, lang='fr')
    Mois=['janvier','fevrier','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','Decembre']
    month = int(interrogatoire.dateCreation.strftime("%m"))
    mois = Mois[month-1]
    hour = interrogatoire.dateCreation.strftime("%H")
    heure =num2words(hour, lang='fr')
    m=interrogatoire.dateCreation.strftime("%M")
    print(m)
    minutes = num2words(m, lang='fr')
    template_path = 'interrogatoire/interrogatoirePDF.html'
    context = {'pv':interrogatoire,'annee':annee,'jour':jour,'mois':mois,'heure':heure, 'minutes':minutes}
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

"""Confrontation"""
@login_required(login_url='login:judiciaire')
def confrontation(request):
    listConfrontation = Confrontation.objects.all
    context = {
        'listConfrontation': listConfrontation
    }
    return render(request, 'confrontation/confrontation.html',context);
@login_required(login_url='login:judiciaire')
def detailConfrontation(request, pv_id):
    try:
        pv = Confrontation.objects.get(pk=pv_id)
    except Confrontation.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'confrontation/detail_confrontation.html', {'pv': pv})
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
def deleteConfrontation(request,pv_id):
    pv = Confrontation.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:confrontation')
@login_required(login_url='login:judiciaire')
def render_pdf_confrontation(request,id):
    confrontation=Confrontation.objects.get(pk=id)
    print(num2words(42, lang='fr'))
    year = confrontation.dateCreation.strftime("%Y")
    annee =num2words(year, lang='fr')
    day =confrontation.dateCreation.strftime("%d")
    jour = num2words(day, lang='fr')
    Mois=['janvier','fevrier','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','Decembre']
    month = int(confrontation.dateCreation.strftime("%m"))
    mois = Mois[month-1]
    hour = confrontation.dateCreation.strftime("%H")
    heure =num2words(hour, lang='fr')
    m=confrontation.dateCreation.strftime("%M")
    print(m)
    minutes = num2words(m, lang='fr')
    template_path = 'confrontation/confrontationPDF.html'
    context = {'pv':confrontation,'annee':annee,'jour':jour,'mois':mois,'heure':heure, 'minutes':minutes}
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

"""Fin Confrontation"""
"""Mission"""
@login_required(login_url='login:judiciaire')
def mission(request):
    listMission = Mission.objects.all
    context = {
        'listMission': listMission
    }
    return render(request, 'mission/mission.html',context);
@login_required(login_url='login:judiciaire')
def detailMission(request, pv_id):
    try:
        pv = Mission.objects.get(pk=pv_id)
    except Interrogatoire.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'mission/detail_mission.html', {'pv': pv})
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
def deleteMission(request,pv_id):
    pv = Mission.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:mission')
@login_required(login_url='login:judiciaire')
def render_pdf_mission(request,id):
    mission=Mission.objects.get(pk=id)
    print(num2words(42, lang='fr'))
    year = mission.dateCreation.strftime("%Y")
    annee =num2words(year, lang='fr')
    day =mission.dateCreation.strftime("%d")
    jour = num2words(day, lang='fr')
    Mois=['janvier','fevrier','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','Decembre']
    month = int(mission.dateCreation.strftime("%m"))
    mois = Mois[month-1]
    hour = mission.dateCreation.strftime("%H")
    heure =num2words(hour, lang='fr')
    m=mission.dateCreation.strftime("%M")
    print(m)
    minutes = num2words(m, lang='fr')
    template_path = 'mission/missionPDF.html'
    context = {'pv':mission,'annee':annee,'jour':jour,'mois':mois,'heure':heure, 'minutes':minutes}
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

"""Fin Mission"""
"""Requisition"""
@login_required(login_url='login:judiciaire')
def requisition(request):
    listRequisition = Requisition.objects.all
    context = {
        'listRequisition': listRequisition
    }
    return render(request, 'requisition/requisition.html',context);
@login_required(login_url='login:judiciaire')
def detailRequisition(request, pv_id):
    try:
        pv = Requisition.objects.get(pk=pv_id)
    except Requisition.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'requisition/detail_requisition.html', {'pv': pv})
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
def deleteRequisition(request,pv_id):
    pv = Requisition.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:requisition')
@login_required(login_url='login:judiciaire')
def render_pdf_requisition(request,id):
    requisition=Requisition.objects.get(pk=id)
    print(num2words(42, lang='fr'))
    year = requisition.dateCreation.strftime("%Y")
    annee =num2words(year, lang='fr')
    day =requisition.dateCreation.strftime("%d")
    jour = num2words(day, lang='fr')
    Mois=['janvier','fevrier','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','Decembre']
    month = int(requisition.dateCreation.strftime("%m"))
    mois = Mois[month-1]
    hour = requisition.dateCreation.strftime("%H")
    heure =num2words(hour, lang='fr')
    m=requisition.dateCreation.strftime("%M")
    print(m)
    minutes = num2words(m, lang='fr')
    template_path = 'requisition/requisitionPDF.html'
    context = {'pv':requisition,'annee':annee,'jour':jour,'mois':mois,'heure':heure, 'minutes':minutes}
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

"""Fin Requisition"""
"""Conduite"""
@login_required(login_url='login:judiciaire')
def conduite(request):
    listConduite = Conduite.objects.all
    context = {
        'listConduite': listConduite
    }
    return render(request, 'conduite/conduite.html',context);
@login_required(login_url='login:judiciaire')
def detailConduite(request, pv_id):
    try:
        pv = Conduite.objects.get(pk=pv_id)
    except Conduite.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'conduite/detail_conduite.html', {'pv': pv})
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
def deleteConduite(request,pv_id):
    pv = Conduite.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:conduite')

@login_required(login_url='login:judiciaire')
def render_pdf_conduite(request,id):
    conduite=Conduite.objects.get(pk=id)
    print(num2words(42, lang='fr'))
    year = conduite.dateCreation.strftime("%Y")
    annee =num2words(year, lang='fr')
    day =conduite.dateCreation.strftime("%d")
    jour = num2words(day, lang='fr')
    Mois=['janvier','fevrier','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','Decembre']
    month = int(conduite.dateCreation.strftime("%m"))
    mois = Mois[month-1]
    hour = conduite.dateCreation.strftime("%H")
    heure =num2words(hour, lang='fr')
    m=conduite.dateCreation.strftime("%M")
    print(m)
    minutes = num2words(m, lang='fr')
    template_path = 'conduite/conduitePDF.html'
    context = {'pv':conduite,'annee':annee,'jour':jour,'mois':mois,'heure':heure, 'minutes':minutes}
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

"""Fin Conduite"""
"""Cloture"""
@login_required(login_url='login:judiciaire')
def cloture(request):
    listCloture = Cloture.objects.all
    context = {
        'listCloture': listCloture
    }
    return render(request, 'cloture/cloture.html',context);
@login_required(login_url='login:judiciaire')
def detailCloture(request, pv_id):
    try:
        pv = Cloture.objects.get(pk=pv_id)
    except Cloture.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'cloture/detail_cloture.html', {'pv': pv})
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
def deleteCloture(request,pv_id):
    pv = Cloture.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:cloture')
@login_required(login_url='login:judiciaire')
def render_pdf_cloture(request,id):
    cloture=Cloture.objects.get(pk=id)
    print(num2words(42, lang='fr'))
    year = cloture.dateCreation.strftime("%Y")
    annee =num2words(year, lang='fr')
    day =cloture.dateCreation.strftime("%d")
    jour = num2words(day, lang='fr')
    Mois=['janvier','fevrier','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','Decembre']
    month = int(cloture.dateCreation.strftime("%m"))
    mois = Mois[month-1]
    hour = cloture.dateCreation.strftime("%H")
    heure =num2words(hour, lang='fr')
    m=cloture.dateCreation.strftime("%M")
    print(m)
    minutes = num2words(m, lang='fr')
    template_path = 'cloture/cloturePDF.html'
    context = {'pv':cloture,'annee':annee,'jour':jour,'mois':mois,'heure':heure, 'minutes':minutes}
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

"""Fin Cloture"""
"""Notifification à Garde à vue"""
@login_required(login_url='login:judiciaire')
def notification(request):
    listNotification = Notification.objects.all
    context = {
        'listNotification': listNotification
    }
    return render(request, 'notification/notification.html',context);
@login_required(login_url='login:judiciaire')
def detailNotification(request, pv_id):
    try:
        pv = Notification.objects.get(pk=pv_id)
    except Notification.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'notification/detail_notification.html', {'pv': pv})
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
def deleteNotification(request,pv_id):
    pv = Notification.objects.get(pk=pv_id)
    pv.delete()
    return redirect('judiciaire:notification')
@login_required(login_url='login:judiciaire')
def render_pdf_notification(request,id):
    notification=Notification.objects.get(pk=id)
    print(num2words(42, lang='fr'))
    year = notification.dateCreation.strftime("%Y")
    annee =num2words(year, lang='fr')
    day =notification.dateCreation.strftime("%d")
    jour = num2words(day, lang='fr')
    Mois=['janvier','fevrier','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','Decembre']
    month = int(notification.dateCreation.strftime("%m"))
    mois = Mois[month-1]
    hour = notification.dateCreation.strftime("%H")
    heure =num2words(hour, lang='fr')
    m=notification.dateCreation.strftime("%M")
    print(m)
    minutes = num2words(m, lang='fr')
    template_path = 'notification/notificationPDF.html'
    context = {'pv':notification,'annee':annee,'jour':jour,'mois':mois,'heure':heure, 'minutes':minutes}
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

""" Fin Notifification à Garde à vue"""

@login_required(login_url='login:judiciaire')
def crime(request):
    listCrime = Crime.objects.all
    context = {
        'listCrime': listCrime
    }
    return render(request, 'enquete.html',context);
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
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
@login_required(login_url='login:judiciaire')
def deleteCrime(id):
    crime = Crime.objects.get(pk=id)
    crime.delete()
    return redirect('judiciaire:crime')
