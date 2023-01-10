# Proyecto_Final_Carros_4
Proyecto final 

#Arrancamos con django

#Proyecto final de coder 

carros.html== <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carros</title>
</head>
<body>

    <h1>Lista de mis Vehiculos</h1>

    {% for vehiculo in lista_carros %}
        <ul>
            <li> Id: {{vehiculo.id}} &nbsp;  Marca: {{vehiculo.marca_del_carro}}, &nbsp;  Modelo:{{vehiculo.modelos_del_carro}},  &nbsp; Color:{{vehiculo.color_del_carro}}  </li>
        </ul>
    {% endfor %}
    
</body>
</html>


buscar_Carros== <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>carros</title>
</head>
<body>
    {{resultado}}
</body>
</html>



buscar_carros2<!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Carros</title>
  </head>
  <body>
      <h1>buscar el carro por el nombre</h1>
    