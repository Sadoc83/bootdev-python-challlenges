""" 
# =========================================================
# Día 19 - Validación de métodos de pago en Urban Routes
# =========================================================

Pondremos en práctica lo aprendido hasta el momento validando distintos datos de Urban Routes.
Debes completar el código para:

* Revisar si el método de pago "tarjeta" está en la lista de métodos de pago. 
Si no está, mostrar una advertencia.

* Recorrer los mensajes de notificación y asegurarte de que cada mensaje contenga la palabra 
"pago". Si no aparece, mostrar una advertencia.

* Revisar la configuración de un viaje y comprobar que la clave "ruta" esté presente. 
Si no está, mostrar una advertencia.

Código inicial

1  # 1. Métodos de pago
2  metodos_pago = ["tarjeta", "efectivo", "paypal"]
3
4  if :
5  	print("Advertencia: falta el método de pago 'tarjeta'.")
6
7  # 2. Notificaciones
8  mensajes = ["Tu pago fue exitoso", "Viaje confirmado"]
9
10 for mensaje in mensajes:
11 	if ...:
12	 	print("Advertencia: el mensaje no contiene la palabra 'pago'.")
13 
14 # 3. Configuración del viaje
15 config_viaje = {
16 	"origen": "Aeropuerto",
17 	"destino": "Hotel",
18 	"hora": "10:30"
19 }
20
21 if ...:
22 	print("Advertencia: falta la clave 'ruta' en la configuración.")

Pista
Usa el operador not in para verificar si "tarjeta" está en la lista. En el bucle, verifica si "pago" no está en cada mensaje. Para el diccionario, recuerda que in y not in revisan las claves, no los valores.

"""

# Código final

    # 1. Métodos de pago
metodos_pago = ["tarjeta", "efectivo", "paypal"]

if "tarjeta" not in metodos_pago:
  	print("Advertencia: falta el método de pago 'tarjeta'.")

    # 2. Notificaciones
mensajes = ["Tu pago fue exitoso", "Viaje confirmado"]

for mensaje in mensajes:
	 if "pago" not in mensaje:
 	       print("Advertencia: el mensaje no contiene la palabra 'pago'.")
 
    # 3. Configuración del viaje
config_viaje = {
 	"origen": "Aeropuerto",
 	"destino": "Hotel",
 	"hora": "10:30"
 }
 
if "ruta" not in config_viaje:
 	print("Advertencia: falta la clave 'ruta' en la configuración.")

"""

Resultado
Advertencia: el mensaje no contiene la palabra 'pago'.
Advertencia: falta la clave 'ruta' en la configuración.


🕵️‍♂️ Análisis de QA: ¿Qué está validando Python aquí?

1. En la Lista ("tarjeta" not in metodos_pago): Python busca el elemento exacto dentro de la 
   colección. Como "tarjeta" sí está en la lista de la línea 51, la condición da Falso (False) 
   y no imprime ninguna advertencia. ¡Prueba superada!

2. En el Texto ("pago" not in mensaje): El bucle for analiza cada string. En la segunda vuelta, 
   el mensaje es "Viaje confirmado". Como la subcadena "pago" no aparece por ningún lado, la 
   condición se vuelve Verdadera (True) y dispara la alerta en la terminal.

3. En el Diccionario ("ruta" not in config_viaje): Al usar not in directamente sobre un diccionario, 
   Python busca exclusivamente entre las claves ("origen", "destino", "hora"). Como la clave "ruta" 
   hace falta en la configuración, la condición se cumple y lanza la advertencia perfectamente.

"""