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
from vehiculo.views import (index, buscar, mostrar_vehiculo, BuscarCarros, AgregarCarro, CarrosCrear, 
ActualizarCarros,DetalleCarros, CarroList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Bienvenida/', index), 
    path("buscar_carros/", buscar),
    path("Carros", mostrar_vehiculo),
    path("Carros/buscar", BuscarCarros.as_view()),
    path("Carros/Agregar", AgregarCarro.as_view()),
    path("Carros/Actualizar/<int:pk>", ActualizarCarros.as_view()),
    path("Carros/<int:pk>/detalle", DetalleCarros.as_view()),
    path("Panel/", CarroList.as_view()),
    path("Panel/Crear", CarrosCrear.as_view())
]

