""" 
=========================================================
Día 17 - Validación de tipo de dato en Urban Routes
=========================================================

Estoy validando la respuesta de la API de Urban Routes.
El valor devuelto para el número de pasajeros es:

passengers = "4"
El objetivo es:
Mostrar el tipo de dato de passengers.

Si passengers no es un número (int), mostrar el mensaje "Data type error!" y detener la ejecución.
Si fuera un número válido, mostrar "Data type OK".

Código inicial

  from sys import exit

  passengers = "4"

  # Paso 1: muestra el tipo de dato
  print(...)

  # Paso 2: valida si es int
  if type(passengers) != int:
      print("Data type error!")
      exit()
  # Paso 3: muestra confirmación
  print("Data type OK")

Pista
Usa type(valor) para comprobar el tipo de una variable. Recuerda que str y int son tipos diferentes.
Si la condición se cumple, exit() detendrá el programa en ese punto.
"""

#Código final
from sys import exit

passengers = "4"

# Paso 1: muestra el tipo de dato
print(type(passengers))

# Paso 2: valida si es int
if type(passengers) != int:
    print("Data type error!")
    exit()
#(Nota: También se puede escribir if type(passengers) is not int: y 
# funcionará exactamente igual de bien).

# Paso 3: muestra confirmación
print("Data type OK")

""" 
Resultado
Traceback (most recent call last):
  File "main.py", line 11, in <module>
    exit()
SystemExit

<class 'str'>
Data type error!
""" 

"""
🕵️‍♂️ El Análisis de QA (Descifrando el Acertijo)

1. La salida de la Línea 43: Al ejecutar print(type(passengers)), la pantalla va a pintar 
<class 'str'> porque el 4 tiene comillas.

2. La trampa del if(la Línea 46): Al evaluar if type(passengers) is not int:, Python dice: 
¿<class 'str'> es diferente de int?. La respuesta es Verdadero (True).

3. El freno de mano (exit()) Línea 48: Al entrar al if, se imprime "Data type error!" y 
la función exit() apaga el programa inmediatamente. Así evitamos que se ejecute la línea 14, 
protegiendo a la API de Urban Routes de procesar datos basura.
"""