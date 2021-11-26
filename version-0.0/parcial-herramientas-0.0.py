##Parcial Herramientas
"""
Codigo hecho por:
Juan Esteban Becerra Gutierrez
ID: 8965694
Alejandro Sarmiento Rivera
ID: 8968284
"""
precios = {"078": 12000, "236": 5400, "728": 7500} ## Un diccionario con las id de los productos y sus respectivos precios.

##Operacion para calcular el precio final del producto.
def descuento(rol, prod, cant):
  Valor = 0 ##Valor inicial para poder usar la variable.

  ##Si el valor se encuentra entre las claves del diccionario.
  if prod in precios:
    v = precios[prod] ##Se extrae el precio del producto.
  
  ##Si el rol del usuario es Estudiante.
  if rol == 1:
    Valor = (v*cant) - ((v*cant)*0.5) ##Se aplica el descuento al precio del producto.
  ##Si el rol del usuario es Profesor.
  elif rol == 2:
    Valor = (v*cant) - ((v*cant)*0.2) ##Se aplica el descuento al precio del producto.

  return Valor

##Operacion para pedir los valores al usuario.
def leerimprimir():
  print("Ingrese cédula:")
  ced = int(input())

  print("\n¿Cuál es su rol?\n1: Estudiante\n2: Profesor")
  rol = int(input())
  
  ##Si el rol del usuario es Estudiante.
  if rol == 1:
    rolp = "estudiante"
  ##Si el rol del usuario es Profesor.
  elif rol == 2:
    rolp = "profesor"
  
  print("\nIngrese código de producto a comprar:")
  prod = str(input())
  
  print("\nIngrese cantidad a comprar:")
  cant = int(input())
  
  val = descuento(rol, prod, cant) ##Se invoca la operacion anterior para hallar el precio final con los datos digitados por el usuario.
  
  print("\nEl",rolp ,"con cedula", ced, "debe pagar", val, "por el producto",prod)
 
leerimprimir() ##Se invoca la ultima operacion para que funcione el programa.
