from django.urls import path

from accident import views

app_name = 'accident'
urlpatterns = [
    path('',views.index),
    #URL Type_Accident
     path('type/enregistrement/',views.save, name='type_accident_save'),
     path('type/detail/<int:pv_id>/', views.detailTypeAccident,name='detail_type_accident'),
     path('type/delete/<int:pv_id>/',views.delete,name='delete_type_accident'),
     path('type/update/<int:pv_id>/',views.update,name='update_type_accident'),
     path('type/',views.typeAccident, name='type_accident'),
     #FIN URL Type_Accident
     # URL Accident
     path('enregistrement/', views.saveAccident, name='accident_save'),
     path('detail/<int:pv_id>/', views.detailAccident, name='detail_accident'),
     path('delete/<int:pv_id>/', views.deleteAccident, name='delete_accident'),
     path('update/<int:pv_id>/', views.updateAccident, name='update_accident'),
     path('accident', views.accident, name='accident'),
     # FIN URL Accident
     # URL VEHICULE
     path('vehicule/enregistrement', views.saveVehicule, name='vehicule_save'),
     # FIN URl VEHICULE
     # URL ACCESSOIRE
     path('vehicule/accessoire',views.saveAccessoire, name='accessoire_save'),
    # FIN URL ACCESSOIRE
    # URL CONDUCTEUR
    path('conducteur/enregistrement',views.saveConducteur, name='conducteur_save'),
    #FIN URL CONDUCTEUR
    # URL VICTIME
    path('victime/enregistrement', views.saveVictime, name='victime_save'),
    #FIN URL VICTIME
    path('temoin/enregistrement', views.saveTemoin, name='temoin_save'),
    path('etat_des_lieux/enregistrement',views.saveEtat, name='etat_save'),
    path('declaration/enregistrement',views.saveDeclaration,name='declaration_save'),
    #URL ACCIDENT MATERIEL
    path('accident_materiel',views.accidentMateriel, name='accident_materiel')


]