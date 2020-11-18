from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sensor/temperature', views.sensort, name='sensort'),
    path('sensor/light', views.sensorl, name='sensorl'),
    path('sensor/humidity', views.sensorh, name='sensorh'),
    # ex: /polls/5/results/
    path('sensor/graphs', views.graficos, name='graph')
]