from datetime import datetime as dt

from django.http import HttpResponse
from django.template import Template, Context, loader

def index(request):
    diccionario = {"nombre" : "Esteban", "apellido" : "Quito"}
    plantilla = loader.get_template("index.html") #Toda la ruta del template esta en el DIRS de settings.
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def saludo(request):
    return HttpResponse("Hola MUNDO")

def segunda_vista(request):
    return HttpResponse("<br><br><h1> Hola de nuevo")

def dia(request):
    hoy = dt.now()
    return HttpResponse(f"El dia y hora actual es: <br> {hoy}")

def mostrar_nombre(request, nombre):
    texto = f"Tu nombre es, {nombre}"
    return HttpResponse(texto)

def probandoTemplate(self):
    miHtml = open("C:/Users/Dawy_/Desktop/project_django/Project/Project/templates/template1.html")
    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1
    #Recordar importar template y contex, con: from django.template import Template, Context
    notas = [10, 8, 3, 9, 6]
    mis_datos = {"nombre" : "Esteban", "apellido" : "Quito", "notas" : notas}
    miContexto = Context(mis_datos) #En este caso no hay nada ya que mp hay parametros, igual hay que crearlo
    documento = plantilla.render(miContexto) #Aca rederizamos la plantilla en documento

    return HttpResponse(documento)

def probandoTemplate2(self):
    notas = [10, 8, 3, 9, 6]
    mis_datos = {"nombre" : "Esteban", "apellido" : "Quito", "notas" : notas}
    
    plantilla = loader.get_template("template1.html") #Toda la ruta del template esta en el DIRS de settings.
    documento = plantilla.render(mis_datos)
    
    return HttpResponse(documento)