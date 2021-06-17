from django.urls import path

from postepolice import views
app_name='poste'
urlpatterns = [
 path('plainte/',views.plainte, name='plainte'),
 path('plainte/enregistrement', views.savePlainte, name='save_plainte'),
 path('plainte/detail/<int:id>/', views.detailPlainte,name='detail_plainte'),
 path('plainte/delete/<int:id>/',views.deletePlainte,name='delete_plainte'),
 path('plainte/update/<int:id>/',views.updatePlainte,name='update_plainte'),

 path('perte/',views.perte, name='perte'),
 path('perte/enregistrement', views.savePerte, name='save_perte'),
 path('perte/detail/<int:id>/', views.detailPerte,name='detail_perte'),
 path('perte/delete/<int:id>/',views.deletePerte,name='delete_perte'),
 path('perte/update/<int:id>/',views.updatePerte,name='update_perte'),

 path('ecrou/',views.ecrou, name='ecrou'),
 path('ecrou/enregistrement', views.saveEcrou, name='save_ecrou'),
 path('ecrou/detail/<int:id>/', views.detailEcrou,name='detail_ecrou'),
 path('ecrou/delete/<int:id>/',views.deleteEcrou,name='delete_ecrou'),
 path('ecrou/update/<int:id>/',views.updateEcrou,name='update_ecrou'),

 path('main_courante/',views.mainCourante, name='main_courante'),
 path('main_courante/enregistrement', views.saveMainCourante, name='save_main_courante'),
 path('main_courante/detail/<int:id>/', views.detailMainCourante,name='detail_main_courante'),
 path('main_courante/delete/<int:id>/',views.deleteMainCourante,name='delete_main_courante'),
 path('main_courante/update/<int:id>/',views.updateMainCourante,name='update_main_courante'),

 path('objet_consigne/',views.objetConsigne, name='objet_consigne'),
 path('objet_consigne/enregistrement', views.saveObjetConsigne, name='save_objet_consigne'),
 path('objet_consigne/detail/<int:id>/', views.detailObjetConsigne,name='detail_objet_consigne'),
 path('objet_consigne/delete/<int:id>/',views.deleteObjetConsigne,name='delete_objet_consigne'),
 path('objet_consigne/update/<int:id>/',views.updateObjetConsigne,name='update_objet_consigne'),

]