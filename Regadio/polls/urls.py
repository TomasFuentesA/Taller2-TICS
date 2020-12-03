from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sensor/temperature', views.sensort, name='sensort'),
    path('sensor/light', views.sensorl, name='sensorl'),
    path('sensor/humidity', views.sensorh, name='sensorh'),
    path('sensor/graphs', views.graficos, name='graph'),
    path('sensor/graphs/light', views.graficoluz, name='graphl'),
    path('sensor/graphs/humidity', views.graficohum, name='graphh'),
    path('sensor/graphs/temperature', views.graficotem, name='grapht')    
]