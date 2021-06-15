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
    path('corporel/enregistrement',views.saveAccidentCorporel,name='accident_corporel_save'),
    path('corporel/vehicule',views.vehiculeCorporelSave,name='vehicule_corporel_save'),
    path('materiel/enregistrement',views.saveAccidentMateriel,name='accident_materiel_save'),
    path('materiel/vehicule',views.vehiculeMatertielSave,name='vehicule_materiel_save'),
    path('temoin',views.temoinMaterielSave,name='temoin_save'),
    path('victime',views.victimeMaterielSave,name='victime_save'),
    path('etat/',views.etatSave,name='etat_save'),
    path('declaration/', views.declarationSave, name='declaration_save'),
    path('liste_accident/', views.accident,name='list_accident'),
    path('detail/<int:accident_id>',views.detailAccident, name='detail_accident'),
    path('update/<int:accident_id>',views.modifierAccident,name='update_accident'),
    path('update/vehicule/<int:vehicule_id>',views.modifierVehicule,name='update_vehicule'),
    path('update/conducteur/<int:conducteur_id>',views.modifierConducteur, name='update_conducteur'),
    path('update/proprietaire/<int:id>',views.modifierProprietaire, name='update_proprietaire'),
    path('update/permis/<int:id>', views.modifierPermis, name='update_permis'),
    path('update/assurance/<int:id>', views.modifierAssurance, name='update_assurance'),
    path('update/victime/<int:id>', views.modifierVictime, name='update_victime'),
    path('update/temoin/<int:id>', views.modifierTemoin, name='update_temoin'),
    path('update/etat_des_lieux/<int:id>', views.modifierEtatDesLieux, name='update_etat_des_lieux'),
    path('update/declaration/<int:id>', views.modifierDeclaration, name='update_declaration'),
    path('update/vitesse/<int:id>', views.modifierVitesse, name='update_vitesse'),
    path('update/eclairege/<int:id>', views.modifierEclairage, name='update_eclairage'),
    path('update/direction/<int:id>', views.modifierDirection, name='update_direction'),
    path('update/essuie_glace/<int:id>', views.modifierEssuieGlace, name='update_essuie_glace'),
    path('update/avertisseur/<int:id>', views.modifierAvertisseur, name='update_avertisseur'),

    #####ULR Suppression
    path('delete/<int:accident_id>', views.deleteAccident, name='delete_accident'),
    ]