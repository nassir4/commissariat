from django.urls import path

from authentification import views

urlpatterns = [
    path('',views.login,),
]