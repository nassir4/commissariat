from pojudiciaire import views
from django.urls import path


app_name = 'judiciaire'
urlpatterns = [

 #URL SAISINE
 path('saisine/enregistrement/<int:id>', views.save, name='save_saisine'),
 path('saisine/detail/<int:pv_id>/', views.detailSaisine, name='detail_saisine'),
 path('saisine/delete/<int:pv_id>/', views.delete, name='delete_saisine'),
 path('saisine/update/<int:pv_id>/', views.update, name='update_saisine'),
 path('saisine/', views.saisine, name='saisine'),
 #FIN URL SAISINE

 #URL AUDITION
 path('audition/enregistrement/<int:id>', views.saveAudition, name='save_audition'),
 path('audition/detail/<int:pv_id>/', views.detailAudition, name='detail_audition'),
 path('audition/delete/<int:pv_id>/', views.deleteAudition, name='delete_audition'),
 path('audition/update/<int:pv_id>/', views.updateAudition, name='update_audition'),
 path('audition/', views.audition, name='audition'),
 #FIN URL AUDITION

 #URL INTERROGATOIRE
 path('interrogatoire/', views.interrogatoire, name='interrogatoire'),
 path('interrogatoire/enregistrement/<int:id>', views.saveInterrogatoire, name='save_interrogatoire'),
 path('interrogatoire/detail/<int:pv_id>/', views.detailInterrogatoire, name='detail_interrogatoire'),
 path('interrogatoire/delete/<int:pv_id>/', views.deleteInterrogatoire, name='delete_interrogatoire'),
 path('interrogatoire/update/<int:pv_id>/', views.updateInterrogatoire, name='update_interrogatoire'),
 #FIN URL INTERROGATOIRE

 #URL CONFRONTATION
 path('confrontation/', views.confrontation, name='confrontation'),
 path('confrontation/enregistrement/<int:id>', views.saveConfrontation, name='save_confrontation'),
 path('confrontation/detail/<int:pv_id>/', views.detailConfrontation, name='detail_confrontation'),
 path('confrontation/delete/<int:pv_id>/', views.deleteConfrontation, name='delete_confrontation'),
 path('confrontation/update/<int:pv_id>/', views.updateConfrontation, name='update_confrontation'),
 #FIN URL CONFRONTATION

 #URL MISSION
 path('mission/', views.mission, name='mission'),
 path('mission/enregistrement/<int:id>', views.saveMission, name='save_mission'),
 path('mission/detail/<int:pv_id>/', views.detailMission, name='detail_mission'),
 path('mission/delete/<int:pv_id>/', views.deleteMission, name='delete_mission'),
 path('mission/update/<int:pv_id>/', views.updateMission, name='update_mission'),
 #FIN  MISSION

 #URL REQUISITION
 path('requisition/', views.requisition, name='requisition'),
 path('requisition/enregistrement/<int:id>', views.saveRequisition, name='save_requisition'),
 path('requisition/detail/<int:pv_id>/', views.detailRequisition, name='detail_requisition'),
 path('requisition/delete/<int:pv_id>/', views.deleteRequisition, name='delete_requisition'),
 path('requisition/update/<int:pv_id>/', views.updateRequisition, name='update_requisition'),
 #FIN URL REQUISITION

 #URL CONDUITE
 path('conduite/', views.conduite, name='conduite'),
 path('conduite/enregistrement/<int:id>', views.saveConduite, name='save_conduite'),
 path('conduite/detail/<int:pv_id>/', views.detailConduite, name='detail_conduite'),
 path('conduite/delete/<int:pv_id>/', views.deleteConduite, name='delete_conduite'),
 path('conduite/update/<int:pv_id>/', views.updateConduite, name='update_conduite'),
 #FIN URL CONDUITE

 #URL NOTIFICATION
 path('notification/', views.notification, name='notification'),
 path('notification/enregistrement/<int:id>', views.saveNotification, name='save_notification'),
 path('notification/detail/<int:pv_id>/', views.detailNotification, name='detail_notification'),
 path('notification/delete/<int:pv_id>/', views.deleteNotification, name='delete_notification'),
 path('notification/update/<int:pv_id>/', views.updateNotification, name='update_notification'),
 #FIN URL NOTIFICATION

 #URL CLOTURE
 path('cloture/', views.cloture, name='cloture'),
 path('cloture/enregistrement/<int:id>', views.saveCloture, name='save_cloture'),
 path('cloture/detail/<int:pv_id>/', views.detailCloture, name='detail_cloture'),
 path('cloture/delete/<int:pv_id>/', views.deleteCloture, name='delete_cloture'),
 path('cloture/update/<int:pv_id>/', views.updateCloture, name='update_cloture'),
 #FIN URL CLOTURE

 path('enquete/', views.crime, name='crime'),
 path('enquete/enregistrement/', views.saveCrime, name='save_crime'),
 path('enquete/detail/<int:id>/', views.detailCrime, name='detail_crime'),
 path('enquete/delete/<int:id>/', views.deleteCrime, name='delete_crime'),
 path('enquete/update/<int:id>/', views.updateCrime, name='update_crime'),

 path('saisine/pdf/<int:id>/', views.render_pdf_saisine, name='pdf_saisine'),
 path('interrogatoire/pdf/<int:id>/', views.render_pdf_interrogatoire, name='pdf_interrogatoire'),
 path('audition/pdf/<int:id>/', views.render_pdf_audition, name='pdf_audition'),
 path('confrontation/pdf/<int:id>/', views.render_pdf_confrontation, name='pdf_confrontation'),
 path('conduite/pdf/<int:id>/', views.render_pdf_conduite, name='pdf_conduite'),
 path('mission/pdf/<int:id>/', views.render_pdf_mission, name='pdf_mission'),
 path('cloture/pdf/<int:id>/', views.render_pdf_cloture, name='pdf_cloture'),
 path('notification/pdf/<int:id>/', views.render_pdf_notification, name='pdf_notification'),
 path('requisition/pdf/<int:id>/', views.render_pdf_requisition, name='pdf_requisition'),
]
