from django.urls import path
from .views import home

#Toda URL criada aqui será acessada a partir de http://localhost:8000/usuarios

urlpatterns = [
    path('', home, name='home_usuarios')  
]
