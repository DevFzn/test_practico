from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Vista desde Servicio de Evaluación Ambiental")

def serv_eval_ambiental(request):
    return render (request, "servEvalAmbient/sevalamb.html")

