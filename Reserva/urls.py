from django.urls import path
from Reserva import views

urlpatterns = [
     path('', views.index, name='index'),
     path('reserva', views.reservar_bici, name='reservar_bici'),
]
