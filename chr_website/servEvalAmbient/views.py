from django.shortcuts import render
from django.http import HttpResponse
from os.path import isfile
from .models import Empresa
from datetime import datetime
import json

def index(request):
    return HttpResponse("Vista desde Servicio de Evaluación Ambiental")

def serv_eval_ambiental(request):
    """
    Vista cuya función es solicitar poblar la base de datos, con los datos del JSON
    """
    read_json('servEvalAmbient/webscrap/datos_sea.json')
    return render (request, "servEvalAmbient/sevalamb.html")

def read_json(json_file):
    """
    Comprueba y lee archivo json pasado como argumento, lo serializa, y llama a
    función json_to_db() con el resultado como argumento
    """
    if isfile(json_file):
        with open(json_file, 'r') as jfile:
            serializado = json.load(jfile)
            json_to_db(serializado)
            #pass
    else:
        print("Archivo no existe: ",json_file)


def json_to_db(serializado):
    """
    Recorre los datos del archivo serializado pasado como argumento y crea una
    nueva instancia de la clase Empresa() port cada "empresa" para finalmente 
    guardarla en la base de datos.
    """
    for dato in serializado:
        new_empresa = Empresa()
        new_empresa.numero = dato['numero']
        new_empresa.nombre = dato['nombre'] 
        new_empresa.tipo = dato['tipo'] 
        new_empresa.region = dato['region']
        new_empresa.tipologia = dato['tipologia']
        new_empresa.titular = dato['titular']
        new_empresa.inversion = dato['inversion']
        date_object = datetime.strptime(dato['fecha'], '%d/%m/%Y')
        new_empresa.fecha = date_object
        new_empresa.estado = dato['estado']
        new_empresa.mapa = dato['mapa']
        new_empresa.save()
        #print(new_empresa)

