from django.urls import path
from .views import home

#Toda URL criada aqui será acessada a partir de http://localhost:8000/dashboard/

urlpatterns = [
    path('', home, name='home_dashboard')  
]