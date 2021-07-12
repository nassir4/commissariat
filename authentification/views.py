from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect


# Create your views here.
from authentification.decorators import unauthenticated_user_accident


def accueil(request):
    return render(request,'accueil.html')
def loginPageSecretaire(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('secretariat:index')
    return render(request,'auth_secretariat.html')
def loginPageAccident(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('accident:list_accident')
    return render(request,'auth_accident.html')
def loginPageJudiciaire(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('judiciaire:crime')
    return render(request,'auth_judiciaire.html')
def loginPagePoste(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('poste:plainte')
    return render(request,'auth_poste.html')
def deconexion(request):
    logout(request)
    return redirect('login:accueil')