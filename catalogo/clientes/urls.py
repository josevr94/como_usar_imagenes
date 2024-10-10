from django.urls import path
from .views import perfil_clientes

urlpatterns = [
    path('perfil/',perfil_clientes,name='perfil')
]