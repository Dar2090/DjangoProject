from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

#Aca se crean las vistas


def saludo(request):
    return HttpResponse("Hola a todos!")

#Ahora generamos como acceder a esta vista, lo hacemos en urls.py


def otra_vista(request):
    return HttpResponse("<h1>Otra vista</h1>")


def fecha_actual(request):
    fecha_actual = datetime.now()
    return HttpResponse(f"<h1>{fecha_actual}</h1>")


def saludo_a(request, nombre):
    nombre_limpio = nombre.replace('-', ' ')
    return HttpResponse(f"Hola {nombre_limpio}!")


def anio_nacimiento(request, edad, nombre):
    nombre_limpio = nombre.replace('-', ' ')
    anio = datetime.now().year - edad
    #anio = fecha.year - int(edad)
    return HttpResponse(f"Hola {nombre_limpio}! Naciste en {anio}")


def probandoTemplate():
    miHtml = open("/home/josue/Escritorio/Django_Project/ClaseDjango/ClaseDjango/plantillas/prueba.html")
    
    plantilla = Template(miHtml.read())

    miHtml.close() #Siempre hay que cerrar los archivos

    miContexto = Context()

    documento = plantilla.render(miContexto) #Aca se renderiza la plantilla

    return HttpResponse(documento)