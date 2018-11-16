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
@login_required(login_url='/auth/login')
def index(request):
	print("hola")
	data={}
	template_name = "index_super_user.html"
	return render(request, template_name,data)

@login_required(login_url='/auth/login')
def reservar_bici(request):
	data={}
	template_name = "reserva.html"
	data["bicicletas"]=Bicicleta.objects.all()
	return render(request, template_name,data)

@login_required(login_url='/auth/login')
def detalle_reserva(request):
	data={}
	template_name = "detalle_reserva.html"

	sucursales = Sucursal.objects.all()
	data['sucursales'] = sucursales
	print (data)
	if (request.POST):
		print(request.POST)
	# if request.POST:
	# 	lista_obj = []
	# 	filtro = []
	# 	print("ASDASDASDA")
	# 	print(request.POST)
	# 	print(request.POST["list_ing"])
	# 	for i in request.POST["list_ing"].split(","):
	# 		if( i != ''):
	# 			filtro.append(i)
	# 	for i in filtro:
	# 		try:
	# 			obj = Ingredients.objects.get(code=i)
	# 			lista_obj.append(obj)
	# 		except:
	# 			raise
	# 	masa = Mass.objects.get(code = request.POST["mass"])
	#
	# 	orden = Pizza(type_mass=masa)
	# 	orden.save()
	# 	for i in lista_obj:
	# 		orden.Ingredient.add(i)
	#
	# 	price = request.POST["price"]
	return render(request, template_name,data)
