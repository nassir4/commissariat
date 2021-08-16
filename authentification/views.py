from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect

from authentification.decorators import unauthenticated_user_accident, unauthenticated_user_secretariat, \
    unauthenticated_user_poste, unauthenticated_user_judiciaire


def accueil(request):
    return render(request,'accueil.html')
@unauthenticated_user_secretariat
def loginPageSecretaire(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('secretariat:index')
    return render(request,'auth_secretariat.html')
@unauthenticated_user_accident
def loginPageAccident(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('accident:list_accident')
    return render(request,'auth_accident.html')
@unauthenticated_user_judiciaire
def loginPageJudiciaire(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('judiciaire:crime')
    return render(request,'auth_judiciaire.html')
@unauthenticated_user_poste
def loginPagePoste(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('poste:liste_registre_Pl')
    return render(request,'auth_poste.html')
def deconexion(request):
    logout(request)
    return redirect('login:accueil')