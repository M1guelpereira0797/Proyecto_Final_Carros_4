from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from mejorado.models import Carro
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from mejorado.forms import UsuarioForm
from mejorado.models import Avatar, Carro, Mensaje
from django.contrib.auth.admin import User

@login_required
def index(request):
    carrox=Carro.objects.order_by("publicado_el").all()
    return render(request, "mejorado/index.html", {"Carro": carrox})

class CarroDetalle(DetailView):
    model= Carro

class Carrolist(ListView):
    model= Carro

class CarroCrear(LoginRequiredMixin, CreateView):
    model = Carro
    success_url= reverse_lazy("listar")
    fields="__all__"

class BorrarCarro(LoginRequiredMixin, DeleteView):
    model = Carro
    success_url= reverse_lazy("listar")
    fields="__all__"


class ActualizarCarro(LoginRequiredMixin, UpdateView):
    model =Carro
    success_url= reverse_lazy("listar")
    fields="__all__"

class UserSingUp(CreateView):
    form_class= UsuarioForm
    template_name="registration/iniciarsesion.html"
    success_url=reverse_lazy("listar")

class Userlogin(LoginView):
    next_page= reverse_lazy ("listar")

class Userlogout(LogoutView):
    next_page= reverse_lazy ("listar")


class AvatarActualizar(UpdateView):
    model=Avatar
    fields= ["imagen"]
    success_url=reverse_lazy("listar")

class UserActualizar(UpdateView):
    model=User
    fields= ["first_name", "last_name", "email"]
    success_url=reverse_lazy("listar")


class MensajeDetalle(DetailView):
    model= Mensaje

class Mensajelist(ListView):
    model= Mensaje

class MensajeCrear(LoginRequiredMixin, CreateView):
    model = Mensaje
    success_url= reverse_lazy("crear")
    fields=["email", "nombre", "texto"]

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url= reverse_lazy("listar")
    