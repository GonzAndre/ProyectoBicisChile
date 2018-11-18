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

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Direccion',)

@admin.register(Tarjeta_credito)
class Tarjeta_creditoAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Numero_tarjeta_redito','Fecha_vencimiento',)

@admin.register(Reserva)
class Reserva(admin.ModelAdmin):
    list_display = ('Fecha_arriendo_inicial','Hora_arriendo_inicial','Fecha_arriendo_final','Hora_arriendo_final','Sucursal_inicio','Sucursal_fin',)

@admin.register(Detalles_reserva)
class Detalles_reservaAdmin(admin.ModelAdmin):
    list_display = ('Cantidad','Bicicleta','Reserva',)

@admin.register(Accesorio)
class AccesorioAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Valor',)
@admin.register(Detalles_accesorios)
class Detalles_accesorioAdmin(admin.ModelAdmin):
    list_display = ('Reserva','Accesorio',)

    # class Accesorio(models.Model):
    #     Nombre = models.CharField(max_length=120)
    #     Valor = models.PositiveIntegerField()
    #
    # class Detalles_accesorios(models.Model):
    #     Reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    #     Accesorio = models.ForeignKey(Accesorio, on_delete=models.CASCADE)
