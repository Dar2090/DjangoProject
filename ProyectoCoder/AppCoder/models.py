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

    
'''Estas son configuraciones nuevas, ahora hay que 
entrar en setting.py y en INSTALLED_APPS cargar nuestra 
app de trabajo, de aqui hay que escribir el comando en 
consola: python3 manage.py makemigrations en la carpeta 
del proyecto. El makemigrations genera codigo para la base
de datos basandose en estos modelos. Se crea un archico
en la carpeta migrations. Luego se ejecuta el comando python3 manage.py migrate para que la BD ejecute este codigo que le envia django'''
 
 
 