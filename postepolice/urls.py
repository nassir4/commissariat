from django.urls import path

from postepolice import views
app_name='poste'
urlpatterns = [
 path('plainte/',views.plainte, name='plainte'),
 path('plainte/enregistrement/<int:id>/', views.savePlainte, name='save_plainte'),
 path('plainte/detail/<int:id>/', views.detailPlainte,name='detail_plainte'),
 path('plainte/delete/<int:id>/',views.deletePlainte,name='delete_plainte'),
 path('plainte/update/<int:id>/',views.updatePlainte,name='update_plainte'),

 path('perte/',views.perte, name='perte'),
 path('perte/enregistrement/<int:id>/', views.savePerte, name='save_perte'),
 path('perte/detail/<int:id>/', views.detailPerte,name='detail_perte'),
 path('perte/delete/<int:id>/',views.deletePerte,name='delete_perte'),
 path('perte/update/<int:id>/',views.updatePerte,name='update_perte'),

 path('ecrou/',views.ecrou, name='ecrou'),
 path('ecrou/enregistrement/<int:id>/', views.saveEcrou, name='save_ecrou'),
 path('ecrou/detail/<int:id>/', views.detailEcrou,name='detail_ecrou'),
 path('ecrou/delete/<int:id>/',views.deleteEcrou,name='delete_ecrou'),
 path('ecrou/update/<int:id>/',views.updateEcrou,name='update_ecrou'),

 path('main_courante/',views.mainCourante, name='main_courante'),
 path('main_courante/enregistrement/<int:id>/', views.saveMainCourante, name='save_main_courante'),
 path('main_courante/detail/<int:id>/', views.detailMainCourante,name='detail_main_courante'),
 path('main_courante/delete/<int:id>/',views.deleteMainCourante,name='delete_main_courante'),
 path('main_courante/update/<int:id>/',views.updateMainCourante,name='update_main_courante'),

 path('objet_consigne/',views.objetConsigne, name='objet_consigne'),
 path('objet_consigne/enregistrement', views.saveObjetConsigne, name='save_objet_consigne'),
 path('objet_consigne/detail/<int:id>/', views.detailObjetConsigne,name='detail_objet_consigne'),
 path('objet_consigne/delete/<int:id>/',views.deleteObjetConsigne,name='delete_objet_consigne'),
 path('objet_consigne/update/<int:id>/',views.updateObjetConsigne,name='update_objet_consigne'),

 path('garde_a_vue/',views.objetConsigne, name='garde'),
 path('garde_a_vue/enregistrement/<int:id>', views.saveGardeAVue, name='save_garde'),
 path('garde_a_vue/detail/<int:id>/', views.detailGardeAVue,name='detail_garde'),
 path('garde_a_vue/update/<int:id>/',views.updateGardeAVue,name='update_garde'),
 path('garde_a_vue/motif/<int:id>/', views.saveGardeAVueMotif, name='motif_garde'),
 path('garde_a_vue/decision/<int:id>/', views.saveGardeAVueDecision, name='decision_garde'),
 path('garde_a_vue/deroulement/<int:id>/', views.saveGardeAVueDeroulement, name='deroulement_garde'),
 path('garde_a_vue/prolongation/<int:id>/', views.saveGardeAVueProl, name='prolongation_garde'),
 path('garde_a_vue/observation/<int:id>/', views.saveGardeAVueObservation, name='observation_garde'),

 path('main_courante/liste_registre/',views.listRegistreMC, name='liste_registre_MC'),
 path('ecrou/liste_registre/',views.listRegistreEc, name='liste_registre_Ec'),
 path('plainte/liste_registre/',views.listRegistrePl, name='liste_registre_Pl'),
 path('perte/liste_registre/',views.listRegistrePer, name='liste_registre_Per'),
 path('garde_a_vue/liste_registre/', views.listRegistreGarde, name='liste_registre_Garde'),

 path('main_courante/registre',views.saveRegistreMC,name='save_registre_mc'),
 path('ecrou/registre',views.saveRegistreEc,name='save_registre_ec'),
 path('plainte/registre',views.saveRegistrePl,name='save_registre_pl'),
 path('perte/registre',views.saveRegistrePer,name='save_registre_per'),
 path('garde_a_vue/registre',views.saveRegistreGarde,name='save_registre_garde'),


 path('main_courante/registre/detail/<int:id>/', views.detailRegistreMC, name='detail_registre_MC'),
 path('plainte/registre/detail/<int:id>/', views.detailRegistrePl, name='detail_registre_Pl'),
 path('perte/registre/detail/<int:id>/', views.detailRegistrePer, name='detail_registre_Per'),
 path('ecrou/registre/detail/<int:id>/', views.detailRegistreEc, name='detail_registre_Ec'),
 path('garde_a_vue/registre/detail/<int:id>/', views.detailRegistreGarde, name='detail_registre_Garde'),

]