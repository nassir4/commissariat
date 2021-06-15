from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect


# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('accident:list_accident')
    return render(request,'base_auth.html')