from django.urls import path

from secretariat import views
from secretariat.views import ChartData, ChartPie

app_name='secretariat'
urlpatterns = [
    path('accueil/', views.index,name='index'),
    path('chartJSON', ChartData.as_view(), name='line_chart_json'),
    path('chartJSSON2',ChartPie.as_view(),name='bar_chart_json'),

    path('plainte/', views.plainte, name='plainte'),
    path('plainte/detail/<int:id>/', views.detailPlainte, name='detail_plainte'),
    path('perte/', views.perte, name='perte'),
    path('perte/detail/<int:id>/', views.detailPerte, name='detail_perte'),
    path('ecrou/', views.ecrou, name='ecrou'),
    path('ecrou/detail/<int:id>/', views.detailEcrou, name='detail_ecrou'),
    path('main_courante/', views.mainCourante, name='main_courante'),
    path('main_courante/detail/<int:id>/', views.detailMainCourante, name='detail_main_courante'),
    path('garde_a_vue/detail/<int:id>/', views.detailGardeAVue, name='detail_garde'),
    path('main_courante/liste_registre/',views.listRegistreMC, name='liste_registre_MC'),
    path('ecrou/liste_registre/',views.listRegistreEc, name='liste_registre_Ec'),
    path('plainte/liste_registre/',views.listRegistrePl, name='liste_registre_Pl'),
    path('perte/liste_registre/',views.listRegistrePer, name='liste_registre_Per'),
    path('garde_a_vue/liste_registre/', views.listRegistreGarde, name='liste_registre_Garde'),

    path('main_courante/registre/detail/<int:id>/', views.detailRegistreMC, name='detail_registre_MC'),
    path('plainte/registre/detail/<int:id>/', views.detailRegistrePl, name='detail_registre_Pl'),
    path('perte/registre/detail/<int:id>/', views.detailRegistrePer, name='detail_registre_Per'),
    path('ecrou/registre/detail/<int:id>/', views.detailRegistreEc, name='detail_registre_Ec'),
    path('garde_a_vue/registre/detail/<int:id>/', views.detailRegistreGarde, name='detail_registre_Garde'),

    path('enquete/enregistrement/', views.saveCrime, name='save_crime'),
    path('enquete/', views.crime, name='crime'),
    path('enquete/detail/<int:id>/', views.detailCrime, name='detail_crime'),
]