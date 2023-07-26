from django.shortcuts import render
from AppTecno.models import *
from django.http import HttpResponse

# Create your views here.

def add_products(request):
    product = Product(name="Mouse1", price="2.60")
    product.save()
    text = f"Se guardo {product.name} y su precio es {product.price}"
    return HttpResponse(text)

def add_employee(request):
    # create a new employee object and save it to the database
    employee = Employee(name="Juan", last_name="Lopez", mail="juanlopez@hotmail.com")
    employee.save()
    text = f"Se guardo el empleado {employee.name} {employee.last_name} con el mail {employee.mail}"
    return HttpResponse(text)