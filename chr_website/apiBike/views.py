#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Vista desde api bike")
#def api_bike(request):
#    return render (request, "apiBike/bikesantiago.html")
