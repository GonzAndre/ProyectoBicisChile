from django.urls import path
from Auth_Reserva import views

urlpatterns = [
    path('login', views.auth_login, name="auth_login"),
    path('logout', views.auth_logout, name="auth_logout"),
]