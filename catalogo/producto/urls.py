from django.urls import path
# from .views import producto_catalogo
from producto import views

urlpatterns = [
    path('catalogo/',views.producto_catalogo,name='catalogo'),
    path('productos/nuevo',views.producto_crear_vistas,name='producto_nuevo')
]