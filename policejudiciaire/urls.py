from django.conf.urls  import url
from . import views
from django.urls import path
app_name = 'judiciaire'
urlpatterns = [

 #URL SAISINE
 path('saisine/enregistrement/',views.save, name='saisine_save'),
 path('saisine/detail/<int:pv_id>/', views.detailSaisine,name='detail_saisine'),
 path('saisine/delete/<int:pv_id>/',views.delete,name='delete_saisine'),
 path('saisine/update/<int:pv_id>/',views.update,name='update_saisine'),
 path('saisine/',views.saisine, name='saisine'),
 #FIN URL SAISINE

 #URL AUDITION
 path('audition/enregistrement/',views.saveAudition, name='save_audition'),
 path('audition/detail/<int:pv_id>/', views.detailAudition,name='detail_audition'),
 path('audition/delete/<int:pv_id>/',views.deleteAudition,name='delete_audition'),
 path('audition/update/<int:pv_id>/',views.updateAudition,name='update_audition'),
 path('audition/',views.audition, name='audition'),
 #FIN URL AUDITION

 #URL INTERROGATOIRE
 path('interrogatoire/',views.interrogatoire, name='interrogatoire'),
 path('interrogatoire/enregistrement', views.saveInterrogatoire, name='save_interrogatoire'),
 path('interrogatoire/detail/<int:pv_id>/', views.detailInterrogatoire,name='detail_interrogatoire'),
 path('interrogatoire/delete/<int:pv_id>/',views.deleteInterrogatoire,name='delete_interrogatoire'),
 path('interrogatoire/update/<int:pv_id>/',views.updateInterrogatoire,name='update_interrogatoire'),
 #FIN URL INTERROGATOIRE

 #URL CONFRONTATION
 path('confrontation/',views.confrontation, name='confrontation'),
 path('confrontation/enregistrement', views.saveConfrontation, name='save_confrontation'),
 path('confrontation/detail/<int:pv_id>/', views.detailConfrontation,name='detail_confrontation'),
 path('confrontation/delete/<int:pv_id>/',views.deleteConfrontation,name='delete_confrontation'),
 path('confrontation/update/<int:pv_id>/',views.updateConfrontation,name='update_confrontation'),
 #FIN URL CONFRONTATION

 #URL MISSION
 path('mission/',views.mission, name='mission'),
 path('mission/enregistrement', views.saveMission, name='save_mission'),
 path('mission/detail/<int:pv_id>/', views.detailMission,name='detail_mission'),
 path('mission/delete/<int:pv_id>/',views.deleteMission,name='delete_mission'),
 path('mission/update/<int:pv_id>/',views.updateMission,name='update_mission'),
 #FIN  MISSION

 #URL REQUISITION
 path('requisition/',views.requisition, name='requisition'),
 path('requisition/enregistrement', views.saveRequisition, name='save_requisition'),
 path('requisition/detail/<int:pv_id>/', views.detailRequisition,name='detail_requisition'),
 path('requisition/delete/<int:pv_id>/',views.deleteRequisition,name='delete_requisition'),
 path('requisition/update/<int:pv_id>/',views.updateRequisition,name='update_requisition'),
 #FIN URL REQUISITION

 #URL CONDUITE
 path('conduite/',views.conduite, name='conduite'),
 path('conduite/enregistrement', views.saveConduite, name='save_conduite'),
 path('conduite/detail/<int:pv_id>/', views.detailConduite,name='detail_conduite'),
 path('conduite/delete/<int:pv_id>/',views.deleteConduite,name='delete_conduite'),
 path('conduite/update/<int:pv_id>/',views.updateConduite,name='update_conduite'),
 #FIN URL CONDUITE

 #URL NOTIFICATION
 path('notification/',views.notification, name='notification'),
 path('notification/enregistrement', views.saveNotification, name='save_notification'),
 path('notification/detail/<int:pv_id>/', views.detailNotification,name='detail_notification'),
 path('notification/delete/<int:pv_id>/',views.deleteNotification,name='delete_notification'),
 path('notification/update/<int:pv_id>/',views.updateNotification,name='update_notification'),
 #FIN URL NOTIFICATION

 #URL CLOTURE
 path('cloture/',views.cloture, name='cloture'),
 path('cloture/enregistrement', views.saveCloture, name='save_cloture'),
 path('cloture/detail/<int:pv_id>/', views.detailCloture,name='detail_cloture'),
 path('cloture/delete/<int:pv_id>/',views.deleteCloture,name='delete_cloture'),
 path('cloture/update/<int:pv_id>/',views.updateCloture,name='update_cloture'),
 #FIN URL CLOTURE

]
