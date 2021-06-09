from django.urls import path

from accident import views

app_name = 'accident'
urlpatterns = [
    path('',views.index),
#############################################################################################################################
################################### URL ACCIDENT MATERIEL ###################################################################
#############################################################################################################################

#############################################################################################################################
################################### URL ACCIDENT MATERIEL ###################################################################
#############################################################################################################################
    path('materiel/enregistrement',views.saveAccidentMateriel,name='accident_materiel_save'),
    path('materiel/vehicule',views.vehiculeMatertielSave,name='vehicule_materiel_save'),
    path('materiel/temoin',views.temoinMaterielSave,name='temoin_materiel_save'),
    path('materiel/temoin/fin',views.temoinEndSave,name='temoin_end_save'),
    path('materiel/victime',views.victimeMaterielSave,name='victime_materiel_save'),
    path('materiel/victime/fin',views.victimeEndSave,name='victime_end_save'),
    path('materiel/etat/',views.etatSave,name='etat_materiel_save'),
    path('materiel/declaration/', views.declarationSave, name='declaration_materiel_save')

]