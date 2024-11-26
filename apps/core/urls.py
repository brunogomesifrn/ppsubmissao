from django.urls import path
from .views import home
from .views import contato, perfil

#Toda URL criada aqui será acessada a partir de http://localhost:8000/

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('perfil/', perfil, name='perfil'),
]
