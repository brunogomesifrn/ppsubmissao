from django.urls import path
from .views import home
from .views import contato

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
]
