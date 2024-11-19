from django.urls import path
from .views import home
from .views import contato

urlpatterns = [
<<<<<<< HEAD
    path('', home, name='home') ,
    path('contato/', contato, name='contato' ),
=======
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
>>>>>>> e47dc81bd6bb72d576420a6f55955370937ed095
]
