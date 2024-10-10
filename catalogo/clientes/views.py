from django.shortcuts import render
from .models import Cliente


def perfil_clientes(request):
    productos = Cliente.objects.all()
    return render(request, 'clientes/perfil.html',{'productos' : productos})
# Create your views here.
