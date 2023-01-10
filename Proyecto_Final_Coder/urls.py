"""Proyecto_Final_Coder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from vehiculo.views import (CarrosCrear, 
#DetalleCarros, CarroList, CarrosBorrar, BorrarCarros, ActualizarCarro)
from mejorado.views import index, Carrolist, CarroCrear, CarroDetalle, BorrarCarro, ActualizarCarro, UserSingUp, Userlogin, Userlogout
from django.contrib.admin.views.decorators import staff_member_required
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('Bienvenida/', index), 
    #path("buscar_carros/", buscar),
    #path("Carros", mostrar_vehiculo),
    #path("Carros/buscar", BuscarCarros.as_view()),
    #path("Carros/Agregar", AgregarCarro.as_view()),
    #path("Carros/Actualizar/<int:pk>", ActualizarCarros.as_view()),
    #path("Carros/Borrar/<int:pk>" , BorrarCarros.as_view()),
    #path("Carros/<int:pk>/detalle", DetalleCarros.as_view()),
    #path("Lista/", CarroList.as_view(), name= "Lista"),
    #path("Lista/Crear", CarrosCrear.as_view()),
    #path("Lista/<int:pk>/borrar" , CarrosBorrar.as_view()),
    #path('Lista/<int:pk>/actualizar', ActualizarCarro.as_view()),
    path("Inicio/", index, name=("Inicio") ),
    path("Inicio/<int:pk>/detalle/", CarroDetalle.as_view(), name=("detalle")),
    path("Inicio/listar/", Carrolist.as_view(), name=("listar")), 
    path("Inicio/crear/", CarroCrear.as_view(), name=("crear")),
    path("Inicio/<int:pk>/actualizar/", ActualizarCarro.as_view(), name=("actualizar")),
    path("Inicio/<int:pk>/borrar", BorrarCarro.as_view(), name=("borrar")),
    path("Inicio/registro/", UserSingUp.as_view(), name=("registro")),
    path("Inicio/login/", Userlogin.as_view(), name=("login")),
    path("Inicio/logout/", Userlogout.as_view(), name=("logout"))

]

