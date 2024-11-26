from django.urls import path
from .views import home
from .views import contato, perfil

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('perfil/', perfil, name='perfil'),
]
