from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso
# Create your views here.

def ver_curso(request):
    curso = Curso(nombre= 'Data Analytics', camada=18980)
    curso.save()
    
    return HttpResponse(f'Nombre de curso: {curso.nombre}, camada: {curso.camada}')

