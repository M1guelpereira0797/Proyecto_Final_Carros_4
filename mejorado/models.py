from django.db import models
from django.contrib.auth.admin import User
class Carro(models.Model):
    Marca_del_Carro = models.CharField(max_length=100)
    Modelo_del_Carro = models.CharField(max_length=100)
    Especificaciones_del_Modelo= models.TextField(max_length= 3000)
    publicado_el= models.DateField()
    imagen = models.ImageField(upload_to="posteos", null="True", blank=True)

class Avatar(models.Model):
    user=models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="avatar")
    imagen = models.ImageField(upload_to="avatares", null="True", blank=True)