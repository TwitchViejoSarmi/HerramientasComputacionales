##Parcial Herramientas
"""
Código hecho por:
Juan Esteban Becerra Gutiérrez
ID: 8965694
Alejandro Sarmiento Rivera
ID: 8968284
"""
precios = {"078": 12000, "236": 5400, "728": 7500}
def descuento(rol, prod, cant):
  Valor = 0
  if prod in precios:
    v = precios[prod]
  if rol == 1:
    Valor = (v*cant) - ((v*cant)*0.5)
  elif rol == 2:
    Valor = (v*cant) - ((v*cant)*0.2)

  return Valor


def leerimprimir():
  print("Ingrese cédula:")
  ced = int(input())
  print("\n¿Cuál es su rol?\n1: Estudiante\n2: Profesor")
  rol = int(input())
  if rol == 1:
    rolp = "estudiante"
  elif rol == 2:
    rolp = "profesor"
  print("\nIngrese código de producto a comprar:")
  prod = str(input())
  print("\nIngrese cantidad a comprar:")
  cant = int(input())
  val = descuento(rol, prod, cant)
  print("\nEl",rolp ,"con cedula", ced, "debe pagar", val, "por el producto",prod)
leerimprimir()