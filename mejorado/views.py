from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from mejorado.models import Carro
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from mejorado.forms import UsuarioForm
def index(request):
    return render(request, "mejorado/index.html")

class CarroDetalle(LoginRequiredMixin, DetailView):
    model= Carro

class Carrolist(LoginRequiredMixin, ListView):
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