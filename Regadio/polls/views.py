from django.http import HttpResponse
from django.template import loader
from .models import *


def index(request):
    template = loader.get_template('polls/index.html')
    context = {}
    riegos = Riego.objects.all()
    mediciones = []
    id_riego=[]
    for ide in riegos:
        id_riego.append(ide.riegoid)

    for i in id_riego:
        mediciones.append(Mediciones.objects.get(id_riego=i))
    time=[]
    for i in mediciones:
        hora=str(i.hora)
        if (len(hora)==4):
            minu = hora[-2:]
            horas = hora[:2]
            lahora= horas+':'+minu
            i.hora = lahora
    
    sesiones_riego=zip(riegos,mediciones)
    temp=[]
    luz=[]
    hum=[]
    datos=Mediciones.objects.all()
    data = {}    
    for i in datos:
        temp.append(i.temperatura)
        hum.append(i.humedad)
        luz.append(i.luz)
    data['tmin']=min(temp)
    data['lmin']=min(luz)
    data['hmin']=min(hum)
    data['tmax']=max(temp)    
    data['lmax']=max(luz)
    data['hmax']=max(hum)
    data['tprom']= sum(temp)/len(temp)    
    data['lprom']= sum(luz)/len(luz)
    data['hprom']= sum(hum)/len(hum)   
    context['data']=data
    context["riegos"]=sesiones_riego
    return HttpResponse(template.render(context, request))

def sensort(request):
    template = loader.get_template('polls/senset.html')
    context ={}
    sensores = Sensores.objects.filter(tipo="temperatura")
    ides = []
    cont = 1
    for _ in sensores:
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
    for _ in sensores:
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
    for _ in sensores:
        ides.append(cont)
        cont+=1
    sensores = zip(ides,sensores)
    context["sensores"] = sensores
    return HttpResponse(template.render(context,request))

def graficos(request):
    template = loader.get_template('polls/graph.html')
    context = {}
   
    return HttpResponse(template.render(context,request))


def graficoluz(request):
    template = loader.get_template('polls/graphl.html')
    context = {}
    horas = []
    data = []
    mediciones = Mediciones.objects.all()
    for i in mediciones:
        a=i.hora
        horas.append(a)
        data.append(i.luz)
    horas.sort()
    context["mediciones"] = data
    context["horas"] = horas
    return HttpResponse(template.render(context,request))

def graficohum(request):
    template = loader.get_template('polls/graphh.html')
    context = {}
    horas = []
    data = []
    mediciones = Mediciones.objects.all()
    for i in mediciones:
        a=i.hora
        horas.append(a)
        data.append(i.humedad)
    horas.sort()
    context["mediciones"] = data
    context["horas"] = horas
    return HttpResponse(template.render(context,request))

def graficotem(request):
    template = loader.get_template('polls/grapht.html')
    context = {}
    horas = []
    data = []
    mediciones = Mediciones.objects.all()
    for i in mediciones:
        a=i.hora
        horas.append(a)
        data.append(i.temperatura)
    horas.sort()
    context["mediciones"] = data
    context["horas"] = horas
    return HttpResponse(template.render(context,request))



