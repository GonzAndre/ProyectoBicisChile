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

	data["accesorios"]=Accesorio.objects.all()
	sucursales = Sucursal.objects.all()
	data['sucursales'] = sucursales
	data['tarjetas'] = Tarjeta_credito.objects.get()
	# print (data)
	# print("user: " + str(request.user.pk))
	if (request.POST):
		bicis_stock = request.POST['bicis']
		sucursal_retiro = request.POST['sucursal_retiro']
		sucursal_entrega = request.POST['sucursal_entrega']
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
		user = User.objects.get(pk=request.user.pk)
		sucursal_inicio = Sucursal.objects.get(pk=sucursal_retiro)
		sucursal_final = Sucursal.objects.get(pk=sucursal_entrega)
		reserva = Reserva(User = user, Fecha_arriendo_inicial = fecha_retiro_final, Hora_arriendo_inicial = hora_retiro_final, Fecha_arriendo_final= fecha_entrega_final, Hora_arriendo_final= hora_entrega_final, Sucursal_inicio = sucursal_inicio, Sucursal_fin = sucursal_final)
		reserva.save()
		bicis_stock = bicis_stock.split(",")
		# stock - PK
		# hay que crear el detalle
		print(bicis_stock)
		print ("PK: "+ str(reserva.pk))

		for i in bicis_stock:
			print("I: " +i)
			cont = 0
			cantidad = 0
			pk_bici = 0
			for n in i.split("-"):
				print ("N: "+n)
				if(cont == 0):
					cantidad = n
					cont = cont + 1
				else:
					pk_bici = n
					print("PK BICI: "+pk_bici)
					bicicleta = Bicicleta.objects.get(pk=pk_bici)
					detalle = Detalles_reserva(Cantidad = cantidad, Bicicleta = bicicleta, Reserva = reserva)
					detalle.save()





		# class Detalles_reserva(models.Model):
		#     Cantidad = models.PositiveIntegerField()
		#     Bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE)
		#     Reserva = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
		#
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
