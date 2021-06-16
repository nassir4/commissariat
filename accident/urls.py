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

    # URL SAISINE
    path('saisine/enregistrement/', views.save, name='saisine_save'),
    path('saisine/detail/<int:pv_id>/', views.detailSaisine, name='detail_saisine'),
    path('saisine/delete/<int:pv_id>/', views.delete, name='delete_saisine'),
    path('saisine/update/<int:pv_id>/', views.update, name='update_saisine'),
    path('saisine/', views.saisine, name='saisine'),
    # FIN URL SAISINE

    # URL AUDITION
    path('plainte/enregistrement/', views.saveAudition, name='save_audition'),
    path('plainte/detail/<int:pv_id>/', views.detailAudition, name='detail_audition'),
    path('plainte/delete/<int:pv_id>/', views.deleteAudition, name='delete_audition'),
    path('plainte/update/<int:pv_id>/', views.updateAudition, name='update_audition'),
    path('audition/', views.audition, name='audition'),
    # FIN URL AUDITION

    # URL INTERROGATOIRE
    path('interrogatoire/', views.interrogatoire, name='interrogatoire'),
    path('interrogatoire/enregistrement', views.saveInterrogatoire, name='save_interrogatoire'),
    path('interrogatoire/detail/<int:pv_id>/', views.detailInterrogatoire, name='detail_interrogatoire'),
    path('interrogatoire/delete/<int:pv_id>/', views.deleteInterrogatoire, name='delete_interrogatoire'),
    path('interrogatoire/update/<int:pv_id>/', views.updateInterrogatoire, name='update_interrogatoire'),
    # FIN URL INTERROGATOIRE

    # URL CONFRONTATION
    path('confrontation/', views.confrontation, name='confrontation'),
    path('confrontation/enregistrement', views.saveConfrontation, name='save_confrontation'),
    path('confrontation/detail/<int:pv_id>/', views.detailConfrontation, name='detail_confrontation'),
    path('confrontation/delete/<int:pv_id>/', views.deleteConfrontation, name='delete_confrontation'),
    path('confrontation/update/<int:pv_id>/', views.updateConfrontation, name='update_confrontation'),
    # FIN URL CONFRONTATION

    # URL MISSION
    path('mission/', views.mission, name='mission'),
    path('mission/enregistrement', views.saveMission, name='save_mission'),
    path('mission/detail/<int:pv_id>/', views.detailMission, name='detail_mission'),
    path('mission/delete/<int:pv_id>/', views.deleteMission, name='delete_mission'),
    path('mission/update/<int:pv_id>/', views.updateMission, name='update_mission'),
    # FIN  MISSION

    # URL REQUISITION
    path('requisition/', views.requisition, name='requisition'),
    path('requisition/enregistrement', views.saveRequisition, name='save_requisition'),
    path('requisition/detail/<int:pv_id>/', views.detailRequisition, name='detail_requisition'),
    path('requisition/delete/<int:pv_id>/', views.deleteRequisition, name='delete_requisition'),
    path('requisition/update/<int:pv_id>/', views.updateRequisition, name='update_requisition'),
    # FIN URL REQUISITION

    # URL CONDUITE
    path('conduite/', views.conduite, name='conduite'),
    path('conduite/enregistrement', views.saveConduite, name='save_conduite'),
    path('conduite/detail/<int:pv_id>/', views.detailConduite, name='detail_conduite'),
    path('conduite/delete/<int:pv_id>/', views.deleteConduite, name='delete_conduite'),
    path('conduite/update/<int:pv_id>/', views.updateConduite, name='update_conduite'),
    # FIN URL CONDUITE

    # URL NOTIFICATION
    path('notification/', views.notification, name='notification'),
    path('notification/enregistrement', views.saveNotification, name='save_notification'),
    path('notification/detail/<int:pv_id>/', views.detailNotification, name='detail_notification'),
    path('notification/delete/<int:pv_id>/', views.deleteNotification, name='delete_notification'),
    path('notification/update/<int:pv_id>/', views.updateNotification, name='update_notification'),
    # FIN URL NOTIFICATION

    # URL CLOTURE
    path('cloture/', views.cloture, name='cloture'),
    path('cloture/enregistrement', views.saveCloture, name='save_cloture'),
    path('cloture/detail/<int:pv_id>/', views.detailCloture, name='detail_cloture'),
    path('cloture/delete/<int:pv_id>/', views.deleteCloture, name='delete_cloture'),
    path('cloture/update/<int:pv_id>/', views.updateCloture, name='update_cloture'),
    # FIN URL CLOTURE


    ]