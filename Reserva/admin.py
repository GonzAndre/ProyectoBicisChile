from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Bicicleta)
class BicicletaAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Modelo','Color','Aro','Estado','Tipo','Codigo','Imagen',)

@admin.register(Cliente)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Fecha_nacimiento','Email','Direccion',)
    
    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
            % (obj.picture.url))