# Herramientas Computacionales
_Por: Alejandro Sarmiento Rivera y Juan Esteban Becerra_

## Problema:

Para recuperarse un poco del tiempo en cuarentena, las cafeterias de la universidad se encuentran dando descuentos a la comunidad estudiantil y dependiendo si es estudiante o profesor, tienen descuentos diferentes. Se desea saber entonces por cada compra cuanto debe pagar el usuario en caja.

## Entradas:

Este algoritmo recibe como entrada los valores:

* **Rol:** El rol que tiene el usuario
* **Ced:** El numero de cedula del usuario.
* **Prod:** El código del producto a comprar.
* **Cant:** Cantidad que se va a comprar del producto.

## Salidas:

Como salida, imprime un mensaje de la siguiente manera:  

"El **_Rol_** con cedula **_Ced_** debe pagar **_Val_** por el producto **_Prod_**"  

Los nuevos valores implementados en la salida son:  

* **Val:** Valor total a pagar por el usuario.

## Procedimiento:

El algoritmo o programa empieza con un diccionario que contiene como claves el ID de los productos y como valores los precios de cada producto.  

Se ejecuta una operacion que recibira los valores digitados por el usuario y los procesara. La operacion establece la variable **_Valor_** en 0 para poder usarla. Luego, ejecuta un condicional que revisa si el numero de producto digitado por el usuario se encuentra entre las claves del diccionario. En caso de que se cumpla, se establece una variable **_v_** cuyo valor sera el valor de la clave digitada por el usuario. Por último, se ejecuta un condicional que revisa si el rol digitado por el usuario fue Estudiante(1) o Profesor(2). En caso de que fuera estudiante, se establece el valor de **_Valor_** como **_v_** multiplicado por la cantidad que se va a comprar del producto **_Cant_** restado por la multiplicación de **_v_**, **_cant_**, y 0.5 que es el descuento aplicado para los estudiantes. En caso de que fuera profesor, se realiza el mismo procedimiento que si fuera estudiante, pero se cambia el 0.5 por 0.2, ya que los profesores tienen un descuento diferente.  

Se ejecuta otra operacion que se encargara de solicitar al usuario que digite los datos necesarios para la solucion y que, dependiendo de los valores digitados, invoque la operacion anterior para imprimir el total a pagar en el texto de salida, junto con toda la informacion digitada.
