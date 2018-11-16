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
	# print (data)
	# print("user: " + str(request.user.pk))
	if (request.POST):
		bicis_stock = request.POST['bicis']
		fecha_retiro = request.POST['fecha_retiro']
		cont = 0
		fecha_retiro_final=""
		hora_retiro_final=""
		#haciendo formato de bd retiro
		for i in fecha_retiro.split(","):
			print("fecha retiro: " + i)
			if (cont==0):
				fecha_retiro_final = fecha_retiro_final + i +"-"
				cont = cont +1
			elif (cont == 1):
				fecha_retiro_final = fecha_retiro_final + i +"-"
				cont = cont +1
			else:
				aux_else = 0
				for n in i.split("T"):
					if (aux_else == 0):
						fecha_retiro_final = fecha_retiro_final + n
						aux_else = aux_else + 1
					else:
						hora_retiro_final = hora_retiro_final + n
		print("fecha retiro final: " +fecha_retiro_final)
		print("hora retiro final: " +hora_retiro_final)




		fecha_entrega = request.POST['fecha_entrega']
		cont = 0
		fecha_entrega_final=""
		hora_entrega_final=""
		#haciendo formato de bd entrega
		for i in fecha_entrega.split(","):
			print("fecha entrega: " + i)
			if (cont==0):
				fecha_entrega_final = fecha_entrega_final + i +"-"
				cont = cont +1
			elif (cont == 1):
				fecha_entrega_final = fecha_entrega_final + i +"-"
				cont = cont +1
			else:
				aux_else = 0
				for n in i.split("T"):
					if (aux_else == 0):
						fecha_entrega_final = fecha_entrega_final + n
						aux_else = aux_else + 1
					else:
						hora_entrega_final = hora_entrega_final + n
		print("fecha entrega final: " +fecha_entrega_final)
		print("hora entrega final: " +hora_entrega_final)
		# sucursal = Sucursal(request.user.pk)

		# class Reserva(models.Model):
		#     User = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_user')
		#     Fecha_arriendo_inicial = models.DateField()
		#     Hora_arriendo_inicial = models.TimeField()
		#     Fecha_arriendo_final = models.DateField()
		#     Hora_arriendo_final = models.TimeField()
		#     Sucursal_inicio = models.ForeignKey(Sucursal, on_delete=models.CASCADE,related_name='%(class)s_inicio')
		#     Sucursal_fin = models.ForeignKey(Sucursal, on_delete=models.CASCADE,related_name='%(class)s_fin')

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
