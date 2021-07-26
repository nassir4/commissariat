from django.urls import path
from authentification import views
app_name = 'login'
urlpatterns = [
    path('',views.accueil,name='accueil'),
    path('postepolice/',views.loginPagePoste, name='poste'),
    path('accident/',views.loginPageAccident, name='accident'),
    path('policejudiciare/',views.loginPageJudiciaire,name='judiciaire'),
    path('secretariat/',views.loginPageSecretaire,name='secretariat'),
    path('logout/',views.deconexion,name='logout'),


]