from django.urls import path
from .views import home
from .views import contato, perfil

urlpatterns = [
<<<<<<< HEAD
    path('', home, name='home') ,
    path('contato/', contato, name='contato' ),
=======
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
<<<<<<< HEAD
    path('perfil/', perfil, name='perfil'),
=======
>>>>>>> e47dc81bd6bb72d576420a6f55955370937ed095
>>>>>>> 709a91b606ec96f4683e9019238efd6accfa6d3f
]
