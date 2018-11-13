from django.urls import path
from Reserva import views

urlpatterns = [
     path('', views.index, name='index'),
     path('reserva', views.reservar_bici, name='reservar_bici'),
     path('detalle_reserva', views.detalle_reserva, name='detalle_reserva'),
]
