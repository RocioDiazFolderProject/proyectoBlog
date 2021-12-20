from django.db import models

# Create your models here.

class Usuario(models.Model) :
    DNI=models.IntegerField()
    Nombre_Completo=models.CharField(max_length=40)
    email=models.EmailField()
    password=models.CharField(max_length=15)
    #Id_Tipo=models.IntegerField()

class Tipo_Usuario(models.Model):
    Id_Tipo=models.IntegerField()
    Tipo_Usuario=models.CharField(max_length=15)

