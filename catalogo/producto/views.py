from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def producto_catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'productos/catalogo.html',{'productos' : productos})


def producto_crear_vistas(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = ProductoForm()    
    return render(request,'productos/producto_crear.html',{'form':form})    




# Create your views here.
