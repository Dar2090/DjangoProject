from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader 

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

nombre = "Pepe"
apellido = "Salterin"
#mis_datos = {'nombre': nombre, 'apellido': apellido}
mi_dict = {'key': 'value'}
mis_datos = {'nombre': nombre, 'apellido': apellido, 'mi_dict': mi_dict, 'lista': [1,2,3,4,5,6]}

def probandoTemplate(self):
    # miHtml = open("/home/josue/Escritorio/Django_Project/ClaseDjango/ClaseDjango/plantillas/prueba.html")
    # plantilla = Template(miHtml.read())
    # miHtml.close() #Siempre hay que cerrar los archivos

    # miContexto = Context({'nombre': nombre, 'apellido': apellido, 'mi_dict': mi_dict, 'lista': [1,2,3,4,5,6]})  #A context se le pasan datos en un dict o mis_datos
    # documento = plantilla.render(miContexto) #Aca se renderiza la plantilla
    
    plantilla = loader.get_template("prueba.html")
    
    documento = plantilla.render(mis_datos) #acepta directamente el diccionario
    
    return HttpResponse(documento)


