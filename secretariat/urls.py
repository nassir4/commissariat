from django.urls import path

from secretariat import views
from secretariat.views import  ChartData

app_name='secretariat'
urlpatterns = [
    path('accueil/', views.index,name='index'),
    path('chartJSON', ChartData.as_view(), name='line_chart_json'),
]