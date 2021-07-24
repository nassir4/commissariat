from django.urls import path

from secretariat import views
from secretariat.views import ChartData, ChartPie

app_name='secretariat'
urlpatterns = [
    path('accueil/', views.index,name='index'),
    path('chartJSON', ChartData.as_view(), name='line_chart_json'),
    path('chartJSSON2',ChartPie.as_view(),name='bar_chart_json')
]