from django.shortcuts import render
from Reserva.models import *
from Reserva.forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

# Create your views here.

def user_cliente(usuario,cliente):
    if(cliente):
        try:
            Cliente.objects.get(usuario=usuario)
            return False
        except Exception as e:
            return True
    else:
        try:
            Cliente.objects.get(usuario=usuario)
            return True
        except Exception as e:
            return False

def user_ejecutivo(user,ejecutivo):
    if(ejecutivo):
        try:
            Ejecutivo.objects.get(usuario=usuario)
            return False
        except Exception as e:
            return True
    else:
        try:
            Ejecutivo.objects.get(usuario=usuario)
            return True
        except Exception as e:
            return False

@login_required(login_url='/auth/login')
def index(request):
    data={}
    data['inicio']=0
    if (user_cliente(request.user,False)):
        data['inicio']= 1
    elif (user_ejecutivo(request.user,False)):
        data['inicio']= 2
    elif (request.user.is_staff == True):
        data['inicio'] = 3
    
    data["request"] = request
    template_name = "index_super_user.html"
    return render(request, template_name,data)

@login_required(login_url='/auth/login')
def reservar_bici(request):
    data={}
    data['inicio'] = 0
    
    if (user_cliente(request.user,False)):
        data['inicio']= 1
    elif (user_ejecutivo(request.user,False)):
        data['inicio']= 2
    elif (request.user.is_staff == True):
        data['inicio'] = 3
        
    data["request"] = request
    template_name = "reserva.html"
    data["bicicletas"]=Bicicleta.objects.all()
    return render(request, template_name,data)