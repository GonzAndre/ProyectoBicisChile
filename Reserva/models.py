from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bicicleta(models.Model):
    Nombre = models.CharField(max_length=120)
    Modelo =  models.CharField(max_length=120)
    Color =  models.CharField(max_length=120)
    Aro =  models.CharField(max_length=120)
    Estado =  models.CharField(max_length=120)
    Tipo =  models.CharField(max_length=120)
    Codigo =  models.CharField(max_length=120)
    Monto_garantia = models.PositiveIntegerField()
    Imagen = models.ImageField(upload_to='image')
    Stock = models.PositiveIntegerField(default=1)

class Cliente(models.Model):
    Nombre = models.CharField(max_length=120)
    Fecha_nacimiento = models.DateField()
    Email = models.EmailField()
    Direccion = models.CharField(max_length=60)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    rut = models.CharField(max_length=8)
    dv = models.PositiveIntegerField()

class Sucursal(models.Model):
    Nombre = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)

class Tarjeta_credito(models.Model):
    Nombre = models.CharField(max_length=25)
    Numero_tarjeta_redito = models.CharField(max_length=19)
    Fecha_vencimiento = models.DateField()

class Reserva(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_user')
    Fecha_arriendo_inicial = models.DateField()
    Hora_arriendo_inicial = models.TimeField()
    Fecha_arriendo_final = models.DateField()
    Hora_arriendo_final = models.TimeField()
    Sucursal_inicio = models.ForeignKey(Sucursal, on_delete=models.CASCADE,related_name='%(class)s_inicio')
    Sucursal_fin = models.ForeignKey(Sucursal, on_delete=models.CASCADE,related_name='%(class)s_fin')

class Detalles_reserva(models.Model):
    Cantidad = models.PositiveIntegerField()
    Bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE)
    Reserva = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
