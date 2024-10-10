from django.contrib import admin
from .models import Producto
from django.utils.html import mark_safe


class ProductoAdmin(admin.ModelAdmin):
    list_display =('nombre','precio','vista_previa')
    def vista_previa(self,obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="100", heigth="100" />')
        return 'No imagen'
    vista_previa.short_description = 'Vista Previa'
    
admin.site.register(Producto, ProductoAdmin)

# Register your models here.
