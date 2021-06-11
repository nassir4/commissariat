from django.urls import path

from accident import views

app_name = 'accident'
urlpatterns = [

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
    path('materiel/declaration/', views.declarationSave, name='declaration_materiel_save'),
    path('liste_accident/', views.accident,name='list_accident'),
    path('detail/<int:accident_id>',views.detailAccident, name='detail_accident'),
    path('update/<int:accident_id>',views.modifierAccident,name='update_accident'),
    path('upadate/vehicule/<int:vehicule_id>',views.modifierVehicule,name='update_vehicule'),
    path('update/conducteur/<int:conducteur_id>',views.modifierConducteur, name='update_conducteur'),
    path('update/proprietaire/<int:id>',views.modifierProprietaire, name='update_proprietaire'),
    path('update/permis/<int:id>', views.modifierPermis, name='update_permis'),
    path('update/assurance/<int:id>', views.modifierAssurance, name='update_assurance'),
    path('update/victime/<int:id>', views.modifierVictime, name='update_victime'),
    path('update/temoin/<int:id>', views.modifierTemoin, name='update_temoin'),
    path('update/etat_des_lieux/<int:id>', views.modifierEtatDesLieux, name='update_etat_des_lieux'),
    path('update/Declaration/<int:id>', views.modifierDeclaration, name='update_declaration'),

    #####ULR Suppression
    path('delete/<int:accident_id>', views.deleteAccident, name='delete_accident'),
    path('delete/vehicule/<int:vehicule_id>', views.deleteVehicule, name='delete_vehicule'),
    path('delete/conducteur/<int:conducteur_id>', views.deleteConducteur, name='delete_conducteur'),
    path('delete/proprietaire/<int:id>', views.deletePropprietaire, name='delete_proprietaire'),
    path('delete/permis/<int:id>', views.deletePermis, name='delete_permis'),
    path('delete/assurance/<int:id>', views.deleteAssurance, name='delete_assurance'),
    path('delete/victime/<int:id>', views.deleteVictime, name='delete_victime'),
    path('delete/temoin/<int:id>', views.deleteTemoin, name='delete_temoin'),
    path('delete/etat_des_lieux/<int:id>', views.deleteEtatDesLieux, name='delete_etat_des_lieux'),
    path('delete/Declaration/<int:id>', views.deleteDeclaraton, name='delete_declaration'),

]