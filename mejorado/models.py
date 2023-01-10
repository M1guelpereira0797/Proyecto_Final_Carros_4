from django.db import models

class Carro(models.Model):
    Marca_del_Carro = models.CharField(max_length=100)
    Modelo_del_Carro = models.CharField(max_length=100)
    Especificaciones_del_Modelo= models.TextField(max_length= 3000)
    publicado_el= models.DateField()
