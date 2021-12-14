from django.db import models

# Create your models here. Los modelos son clases. Guardan la estructura de datos del proyecto

class Curso(models.Model): # Hereda de models, para que tenga funcionalidades basicas
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()
    #python genera automaticamente el id
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
   
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    profesion = models.CharField(max_length=20)
    
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fecha = models.DateField()
    entregado = models.BooleanField()

    
