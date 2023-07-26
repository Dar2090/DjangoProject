from django.db import models

# Create your models here.

'''class Person:
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mail = models.EmailField(default="example@example.com")'''

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mail = models.EmailField(default="example@example.com")

class Client(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mail = models.EmailField(default="example@example.com")
    