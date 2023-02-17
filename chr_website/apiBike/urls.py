from django.urls import path
from apiBike import views

urlpatterns = [
    path('', views.index, name='index')
]
