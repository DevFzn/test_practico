from django.urls import path
from apiBike import views

urlpatterns = [
    path('', views.api_bike, name='api_bike')
    #path('', views.index, name='index')
]
