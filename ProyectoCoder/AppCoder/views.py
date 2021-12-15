from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso
# Create your views here.

def crear_curso(request):
    curso = Curso(nombre= 'Data Analytics', camada=18980)
    curso.save()
    
    return HttpResponse(f'Nombre de curso: {curso.nombre}, camada: {curso.camada}')
# Esto me carga algo nuevo en la BD pero cada vez que lo uso me lo guarda en duplicado.

def ver_curso(request):
    cursos = Curso.objects.all()
    #cursos = cursos.last()
    texto = ''
    
    for curso in cursos:
        texto += f'Curso: {curso.nombre}<br>'
    
    return HttpResponse(f'{texto}')
