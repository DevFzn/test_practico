from django.urls import path
from servEvalAmbient import views

urlpatterns = [
    #path('', views.index, name='index')
    path('', views.serv_eval_ambiental, name='serv_eval_ambient')
]
