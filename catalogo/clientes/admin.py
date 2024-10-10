from django.contrib import admin
from .models import Cliente
from django.utils.html import mark_safe


class ClienteAdmin(admin.ModelAdmin):
    list_display =('nombre','email','vista_previa')
    def vista_previa(self,obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="100", heigth="100" />')
        return 'No imagen'
    vista_previa.short_description = 'Vista Previa'
    
admin.site.register(Cliente,ClienteAdmin)
# Register your models here.
