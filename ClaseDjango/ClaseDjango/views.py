from django.http import HttpResponse


#Aca se crean las vistas


def saludo(request):
    return HttpResponse("Hola a todos!")

#Ahora generamos como acceder a esta vista, lo hacemos en urls.py