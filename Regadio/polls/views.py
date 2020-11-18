from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': ['a','b','c'],
    }
    return HttpResponse(template.render(context, request))

def sensort(request):
    template = loader.get_template('polls/senset.html')
    context ={}
    return HttpResponse(template.render(context,request))

def sensorl(request):
    template = loader.get_template('polls/sensel.html')
    context ={}
    return HttpResponse(template.render(context,request))

def sensorh(request):
    template = loader.get_template('polls/senseh.html')
    context ={}
    return HttpResponse(template.render(context,request))

def graficos(request):
    template = loader.get_template('polls/graph.html')
    context ={}
    return HttpResponse(template.render(context,request))

