# Parcial Herramientas Computacionales
_Por: Alejandro Sarmiento Rivera y Juan Esteban Becerra_

## Problema:

Para recuperarse un poco del tiempo en cuarentena, las cafeterias de la universidad se encuentran dando descuentos a la comunidad estudiantil y dependiendo si es estudiante o profesor, tienen descuentos diferentes. Se desea saber entonces por cada compra cuanto debe pagar el usuario en caja.

## Entradas:

Este algoritmo recibe como entrada los valores:

* **Rol:** El rol que tiene el usuario
* **Ced:** El numero de cedula del usuario.
* **Prod:** El código del producto a comprar.
* **Cant:** Cantidad que se va a comprar del producto.
* **Tempo:** Condicion para saber si el usuario va a comprar otro producto o no.

## Salidas:

Como salida, imprime un mensaje de la siguiente manera:  

"El **_Rol_** con cedula **_Ced_** debe pagar **_Val_** por los productos: **_Productos_**"  

Los nuevos valores implementados en la salida son:  

* **Val:** Valor total a pagar por el usuario.
* **Productos:** Una lista de todos los productos comprados por el usuario.

## Procedimiento:

El algoritmo o programa empieza con un diccionario que contiene como claves el ID de los productos y como valores los precios de cada producto.  

Se ejecuta una operacion que recibira los valores digitados por el usuario y los procesara. La operacion establece la variable **_Valor_** en 0 para poder usarla. Luego, ejecuta un condicional que revisa si el numero de producto digitado por el usuario se encuentra entre las claves del diccionario. En caso de que se cumpla, se establece una variable **_v_** cuyo valor sera el precio en el valor de la clave digitada por el usuario, ya que el valor de cada clave contiene el nombre del producto y su precio. Se multiplica el precio del producto por la cantidad a comprar y se retorna.

Se ejecuta otra operacion que se encargara de solicitar al usuario que digite los datos necesarios para la solucion y que aplique el descuento al valor total a pagar por el usuario. Se pide al usuario que digite su informacion y el codigo del producto. Si el codigo no se encuentra entre las claves del diccionario, entonces se le pedira al usuario que digite el codigo del producto nuevamente. Una vez que digite correctamente el codigo, se le pedira que digite la cantidad a comprar y se invocara la operacion anterior para sumar el precio final del producto con el valor total a pagar. Se le preguntara al usuario si quiere ingresar mas prodcutos. En caso positivo, se le volvera a pedir que ingrese el codigo del producto y la cantidad a comprar, al igual que la invocacion de la operacion anterior. En caso negativo, se aplica un condicional para saber si el usuario es estudiante o profesor. Dependiendo del rol que tenga, se le aplicara el descuento respectivo al valor total a pagar y se imprime el mensaje final.

