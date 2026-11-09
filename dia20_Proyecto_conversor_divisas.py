# =========================================================
# Proyecto del Día 20: Comversor / Cambio de Divisas
# =========================================================

""" 

Aclaración
Este un poco ambioioso proyecto, va a estar **detalladamente explicado** con instrucciones para 
cada una de las celdas. A medida que se avance en los proyectos posteriores, los proyectos 
serán menos guiados, y más complejos. Este proyecto es sencillo para comenzar con algo 
fácil, y además porque aún estoy aprendiendo las herramientas básicas como para hacer programas 
más funcionales, pero aún así te vas a sorprender de lo que puedo lograr con esto resulto ser un un 
buen desafío.


### Consigna.
Voy a crear un código que simule el funcionamiento de una **máquina de cambio de divisas**. 
Por el momento esta máquina sólo recibe **dólares** y devuelve **euros** ¡No es poco para ser 
mí primer programa!

Tu máquina va a necesitar disponer de variables que le brinden la siguiente información:
- Nombre del usuario
- Fecha en que se realiza la operación
- Momento del día (día, tarde o noche)
- Cantidad de dólares a cambiar

Con todo eso, la máquina va a imprimir en pantalla (en diferentes líneas por supuesto) 
un mensaje que incluya los siguientes requisitos:

- Un saludo de bienvenida
- Información de la cantidad de dolares que va a entregar el usuario
- Información de la cantidad de euros que va a recibir
- Detalle específico de cuántos billetes de €10, de €1, y el saldo en monedas que le serán entregados
- Un saludo de despedida

### Nota importante
No hay una única manera de hacer esto. En programación siempre hay muchos caminos para lograr el 
mismo objetivo. Por lo pronto es logres cumplir con la consigna, cualquier abordaje (sensato) 
es válido.

En las siguientes celdas aordaré las instrucciones específicas para que puedas rastrear el proyecto 
paso a paso. Esto funcionará algo parecido como habalr en voz alta y notas a la vez.

### Nota sumer-mega-archi-requetecontra importante
La idea no sólo es aprender, sino fundamentalmente divertirse. Programar es hermoso, es desafiante, 
es la oportunidad de concentrarme en un problema y poner lo mejor de mí para resolverlo.

Eso no significa que si no lo puedo resolver a la primera 
(o segunda, jajajaja :D) no me voy a divertir. Todo lo contrario. 

Si bien resolver problemas por uno mismo es emocionante y excitante, una de las sensaciones 
más placenteras que he experimentado, es creer que algo es imposible, y que luego alguien en quien 
confío me muestre el camino para lograrlo. Se llama "momento Eureka" o aprendizaje significativo 
-aprender haciendo-.

"""

## Instrucciones paso a paso

# 1. Escribir el código necesario para saludar al usuario, antes de comenzar sus operaciones. 
# Es necesario crear tres variables que contengan, respectivamente, el **nombre** del usuario, 
# la **fecha** del día en que está haciendo la operación, y un **saludo** que puede ser *Buenos días*, 
# *Buenas tardes* o *Buenas noches*.

user_name = "Sadoc"
date = "9 de Octubre"
saludo = "Quiubas que mas!!"

# 2. Vamos a una variable llamada **bienvenida** que concatene toda la información anterior en un 
# solo mensaje que salude al usuario  que va a usar el servicio de cambio de divisas. 
# Yo pondré con algo de "chispa"

# **Pista**: Que no se me olvide, segun las insteucciones de la lección las operaciones básicas que 
# ya debería conocer como lo son las de concatenar strings para formar una sola cadena de texto.

bienvenida = saludo + " " + user_name + ", hoy es " + date + ", Bienvenido al servicio de divisas!"
bienvenida

# 3. Siguiente variable numérica llamada **dolares** que almacene la cantidad de dólares usaré 
# para cambiar esos dichosos euros. Importante: los valores en *moneda* suelen expresarse con números 
# decimales, por lo que sería ideal utilizar un valor de tipo **float**.

dolares = 210
dolares

# 4. Siguiente variable llamada **euros_a_recibir** para guarde el resultado de calcular cuántos 
# euros corresponden para la cantidad de dolares ingresada en la variable **dolares**. 
# El tipo de cambio que usaremos es de *0.88*.

euros_a_recibir = dolares * 0.88 
euros_a_recibir

# 5. Nuestra máquina (imaginaria), solo entrega billetes de €10, y de €1 (los decimales los entregará 
# en monedas). Vamos por las 3 variables para cada uno de esos valores (**billetes_10**, 
# **billetes_1** y **monedas**), que contengan los cálculos necesarios para saber cuánto valor 
# en monedas, y cuántos billetes de cada tipo recibirá el usuario.

billetes_10 = euros_a_recibir // 10 
billetes_10

billetes_1 = (euros_a_recibir - (billetes_10 * 10)) // 1
billetes_1

monedas = euros_a_recibir % 1 
monedas

# 6. Para rematar ahora toca escibir una serie de declaraciones **print()** que expresen el mensaje 
# completo, mostrando los siguientes elementos:

"""
- Mensaje de bienvenida
- Información sobre los dólares que entregará
- Información sobre los euros que recibirá
- Detalle de billetes y monedas que le serán entregados
- Saludo de despedida

**Importante**: Cómo aún no llego a la lección de como concatenar números y texto en la misma 
línea de impresión, en muchas ocaciones deberás crear líneas separadas para que el mensaje se 
muestre como en el siguiente ejemplo:


Dolares a entregar:
150.45
"""

print(bienvenida)
print("----------------------------------------")
print("Dolares a entregar:")
print(dolares)
print("----------------------------------------")
print("Euros a recibir en total:")
print(euros_a_recibir)
print("----------------------------------------")
print("Detalle de entrega:")
print("Billetes de €10:")
print(billetes_10)
print("Billetes de €1:")
print(billetes_1)
print("Saldo en monedas:")
print(monedas)
print("----------------------------------------")
print("¡Gracias por usar Urban Exchances, vuelve pronto! " + user_name + ".")

# Resultado en pantalla:
"""
Quiubas que mas!! Sadoc, hoy es 9 de Octubre, Bienvenido al servicio de divisas!
----------------------------------------
Dolares a entregar:
210
----------------------------------------
Euros a recibir en total:
184.8
----------------------------------------
Detalle de entrega:
Billetes de €10:
18.0
Billetes de €1:
4.0
Saldo en monedas:
0.8000000000000114
----------------------------------------
¡Gracias por usar Urban Exchances, vuelve pronto! Sadoc.

"""

# 🧠 ¿Por qué este formato corre sin errores?

# • Paso a paso evité la fusión rota: Al poner el texto arriba y la variable numérica en su propio 
#   print() abajo, la máquina no tiene que pelearse intentando sumar letras con números.
# • Hilos de memoria conectados: Al ejecutar todo en este orden exacto, la variable dolares nacerá 
#   antes de que el print intente llamarla, eliminando por completo algún NameError.
