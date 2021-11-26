##Parcial Herramientas
"""
Codigo hecho por:
Juan Esteban Becerra Gutierrez
ID: 8965694
Alejandro Sarmiento Rivera
ID: 8968284
"""
precios = {"078": ["Coca-Cola", 12000], "236": ["Papas", 5400], "728": ["Empanadas", 7500]} ## Un diccionario con las id de los productos, sus nombres y sus precios.

##Operacion para calcular el precio final por producto.
def descuento(prod, cant):
  Valor = 0 ##Valor inicial para poder usar la variable.

  ##Si el valor se encuentra entre las claves del diccionario.
  if prod in precios:
    v = precios[prod][1] ##Se extrae el precio del producto.
  
  Valor = (v*cant) ##Se multiplica el precio por la cantidad pedida del producto.
  

  return Valor

##Operacion para pedir los valores al usuario y aplicar los descuentos.
def leerimprimir():

  val = 0 ##Valor inicial para poder usar la variable.

  productos = [] ##Lista que corresponde a los productos comprados por el usuario.

  print("Ingrese cedula:")
  ced = int(input())

  print("\n¿Cual es su rol?\n1: Estudiante\n2: Profesor")
  rol = int(input())

  tempo = "a" ##Se da un valor inicial que cumpla la condicion del ciclo para que este funcione.

  ##Mientras el usuario NO haya digitado n en la ultima pregunta.
  while tempo != "n":

    print("\nIngrese codigo de producto a comprar:")
    prod = str(input())

    ##Se le pedira al usuario que digite el codigo del producto mientras el que haya digitado con anterioridad no se encuentre entre las claves del diccionario.
    while prod not in precios:
      print("\nProducto no encontrado")
      print("\nIngrese codigo de producto a comprar")
      prod = str(input())
      
    productos.append(precios[prod][0]) ##Se inserta el producto comprado en la lista de productos comprados.

    print("\nIngrese cantidad a comprar:")
    cant = int(input())
    val += descuento(prod, cant) ##Se invoca la operacion anterior para ir sumando los valores finales de cada producto al valor total.

    print("\n¿Ingresar mas productos? y/n:")
    tempo = str(input()) ##Variable encargada de la condicion del ciclo while.

  ##Si el rol del usuario es Estudiante.
  if rol == 1:
    rolp = "estudiante"
    val = val - (val * 0.5) ##Se aplica el descuento al precio total.
  ##Si el rol del usuario es Profesor.
  elif rol == 2:
    rolp = "profesor"
    val = val - (val * 0.2) ##Se aplica el descuento al precio total.

  print("\nEl",rolp ,"con cedula", ced, "debe pagar", val, "por los productos:",", ".join(productos)) ##Se usa el .join() para convertir la lista en cadena y separar los valores por comas.

leerimprimir() ##Se invoca la ultima operacion para que funcione el programa.
