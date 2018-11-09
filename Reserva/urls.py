from django.urls import path
from Reserva import views

urlpatterns = [
     path('', views.index, name='index'),
]