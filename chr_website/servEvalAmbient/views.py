#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Vista desde Servicio de Evaluación Ambiental")
