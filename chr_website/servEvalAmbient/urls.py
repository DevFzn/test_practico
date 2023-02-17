from django.urls import path
from servEvalAmbient import views

urlpatterns = [
    path('', views.index, name='index')
]
