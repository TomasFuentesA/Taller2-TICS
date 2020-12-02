from django.http import HttpResponse
from django.template import loader
from .models import *


def index(request):
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': ['a','b','c'],
    }
    return HttpResponse(template.render(context, request))

def sensort(request):
    template = loader.get_template('polls/senset.html')
    context ={}
    sensores = Sensores.objects.filter(tipo="temperatura")
    ides = []
    cont = 1
    for i in sensores:
        ides.append(cont)
        cont+=1
    sensores = zip(ides,sensores)
    context["sensores"] = sensores
    return HttpResponse(template.render(context,request))

def sensorl(request):
    template = loader.get_template('polls/sensel.html')
    context ={}
   # Sensor.objects.create(id= asdsad, tipo = asdsad, estado= asdsa) # crear
   # Sensor.objects.all() Retrieve all objects on Table
   # Sensor.objects.get(id=1) Retrieve one object
   # Sensor.objects.filter(estado=0)
    sensores = Sensores.objects.filter(tipo="luz")
    ides = []
    cont = 1
    for i in sensores:
        ides.append(cont)
        cont+=1
    sensores = zip(ides,sensores)
    context["sensores"] = sensores
    return HttpResponse(template.render(context,request))

def sensorh(request):
    template = loader.get_template('polls/senseh.html')
    context ={}
    sensores = Sensores.objects.filter(tipo="humedad")
    ides = []
    cont = 1
    for i in sensores:
        ides.append(cont)
        cont+=1
    sensores = zip(ides,sensores)
    context["sensores"] = sensores
    return HttpResponse(template.render(context,request))

def graficos(request):
    template = loader.get_template('polls/graph.html')
    context ={}
    return HttpResponse(template.render(context,request))

