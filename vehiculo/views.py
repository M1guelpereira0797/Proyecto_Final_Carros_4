from django.shortcuts import render, get_object_or_404
from vehiculo.models import Vehiculo
#from vehiculo.forms import Buscar, CarrosForm
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

#def index(request):
 #   return render(request, "vehiculo/saludar.html")

#def mostrar_vehiculo(resquest):
 #   lista_carros = Vehiculo.objects.all()
  #  return render(resquest, "vehiculo/vehiculo.html" , {"lista_carros": lista_carros})

#def buscar(resquest):
 #   lista_carros=["Mercedes", "Ferrari", "Lamborgini", "Mclaren", "Chevrolet"]
  #  query=resquest.GET["q"]
   # if query in lista_carros:
    #    indice_de_resultado = lista_carros.index(query)
     #   resultado=lista_carros[indice_de_resultado]
    #else: 
     #   resultado= "no hay registro en la base de datos"
    #return render(resquest, 
    #"vehiculo/buscar_vehiculo.html",
    #{"resultado": resultado})

#class BuscarCarros(View):
 #   form_class = Buscar
  #  template_name = 'vehiculo/buscar_vehiculo2.html'
   # initial = {"marca_del_carro":""}
   # def get(self, request):
    #    form = self.form_class(initial=self.initial)
     #   return render(request, self.template_name, {'form':form})
    #def post(self, request):
     #   form = self.form_class(request.POST)
      #  if form.is_valid():
       #     marca_del_carro = form.cleaned_data.get("marca_del_carro")
        #    lista_carros = Vehiculo.objects.filter(marca_del_carro__icontains=marca_del_carro).all() 
         #   form = self.form_class(initial=self.initial)
          #  return render(request, self.template_name, {'form':form, 
         #                                               'lista_carros':lista_carros})
        #return render(request, self.template_name, {"form": form})

#class AgregarCarro(View):

 #   form_class = CarrosForm
  #  template_name = 'vehiculo/agregar_vehiculo.html'
   # initial = {"id":"", "marca_del_carro":"", "modelos_del_carro":"", "color_del_carro":""}

    #def get(self, request):
     #   form = self.form_class(initial=self.initial)
      #  return render(request, self.template_name, {'form':form})

   # def post(self, request):
    #    form = self.form_class(request.POST)
     #   if form.is_valid():
      #      form.save()
       #     msg_exito = f"Se cargo con ??xito el carro {form.cleaned_data.get('nombre')}"
        #    form = self.form_class(initial=self.initial)
         #   return render(request, self.template_name, {'form':form, 
         #                                               'msg_exito': msg_exito})
        
        #return render(request, self.template_name, {"form": form})

#class ActualizarCarros(View):
 # form_class = CarrosForm
 # template_name = 'vehiculo/actualizar_vehiculo.html'
 # initial = {"ID":"", "marca_del_carro":"", "modelos_del_carro":"", "color_del_carro":""}
  
 # def get(self, request, pk): 
  #    vehiculo = get_object_or_404(Vehiculo, pk=pk)
  #    form = self.form_class(instance=vehiculo)
   #   return render(request, self.template_name, {'form':form,'vehiculo': vehiculo})

  #def post(self, request, pk): 
   #   vehiculo = get_object_or_404(Vehiculo, pk=pk)
    #  form = self.form_class(request.POST ,instance=vehiculo)
     # if form.is_valid():
      #    form.save()
       #   msg_exito = f"se actualiz?? con ??xito el carro {form.cleaned_data.get('nombre')}"
        #  form = self.form_class(initial=self.initial)
         # return render(request, self.template_name, {'form':form, 
          #                                            'vehiculo': vehiculo,
           #                                           'msg_exito': msg_exito})
      
      #return render(request, self.template_name, {"form": form})

class BorrarCarros(View):
    template_name = "vehiculo/vehiculo.html"
    def get(self, request, pk):
        vehiculo= get_object_or_404(Vehiculo, pk=pk)
        vehiculo.delete()
        vehiculo= Vehiculo.objects.all()
        return render(request, self.template_name,{"vehiculo": Vehiculo})

class DetalleCarros(DetailView):#listo 
  model = Vehiculo

class CarroList(ListView):#listo
  model = Vehiculo

class CarrosCrear(CreateView):#listo
    model = Vehiculo
    success_url = "/Lista"
    fields = ["marca_del_carro", "modelos_del_carro", "color_del_carro"]

class CarrosBorrar(DeleteView): #listo
    model = Vehiculo
    success_url = "/Lista"

class ActualizarCarro(UpdateView): #listo
  model = Vehiculo
  success_url = "/Lista"
  fields = ["marca_del_carro", "modelos_del_carro", "color_del_carro"]