""" 
=========================================================
Día 18 - Pruebas de rendimiento en Urban Routes
=========================================================

Debemos escribir un programa que recorra la lista response_times y cuente cuántos valores 
son mayores a 500.

Luego imprime el total.

Código inicial

response_times = [120, 640, 510, 200, 999]
slow_count = 0

# Escribe tu código debajo
for time in response_times:
    if time > 500:
        slow_count += 1
print(slow_count)

Pista
Usa un for para recorrer response_times. Dentro del bucle, usa if time > 500. 
Incrementa slow_count con slow_count = slow_count + 1

Este ejercicio es un clásico absoluto de las pruebas de rendimiento (Performance Testing). 
En Urban Routes necesitamos auditar qué tan rápido responde el servidor y contar cuántas 
solicitudes tardaron más de medio segundo (500 ms), lo que en el mundo real calificaría como 
una respuesta lenta ("slow").
Vamos a estructurar el bucle for junto con el condicional if para llenar nuestra alcancía 
slow_count de forma automática.
""" 

# 🛠️ Código final

response_times = [120, 640, 510, 200, 999]
slow_count = 0

for time in response_times:
    if time > 500:
        slow_count = slow_count + 1

print(slow_count)

#Resultado
3

""" 
🕵️‍♂️ Análisis de QA: ¿Cómo trabaja el script tras bambalinas?

El bucle va a tomar los 5 números de la lista, uno por uno, y los pasará por el filtro de aduana 
(if time > 500):

1. 120: ¿Es mayor que 500? Falso. No pasa nada.
2. 640: ¿Es mayor que 500? Verdadero. slow_count sube a 1.
3. 510: ¿Es mayor que 500? Verdadero. slow_count sube a 2.
4. 200: ¿Es mayor que 500? Falso. No pasa nada.
5. 999: ¿Es mayor que 500? Verdadero. slow_count sube a 3.

El Resultado Esperado en la Terminal:
3

Para que la máquina procese este script de QA, hace un viaje fascinante a través de su memoria 
RAM y su procesador (CPU). Vamos a seguir la ejecución línea por línea, paso a paso, tal como 
lo hace el "cerebro" de Python:

📍 Paso 1: Creación del Mapa en la Memoria (Líneas 36 y 37)

Antes de empezar a correr el bucle, la máquina necesita preparar su mesa de trabajo en la 
memoria RAM:

1. Línea 1 (response_times = [...]): La máquina reserva un espacio continuo en la RAM, le pega 
    la etiqueta response_times y guarda ahí los 5 números en orden como si fueran casilleros 
    numerados del 0 al 4.
2. Línea 2 (slow_count = 0): Abre una cajita metálica en la memoria, le escribe afuera con marcador 
    slow_count y mete un 0 adentro. Esta será nuestra alcancía vacía.

🔄 Paso 2: El Desglose del Bucle Vuelta por Vuelta (Líneas 39 a 41)

Aquí el procesador activa un contador interno para recorrer los casilleros de la lista. 
En cada vuelta, crea una variable temporal llamada time donde va metiendo un número a la vez.

🔹 Vuelta 1:

• La máquina va al casillero 0 de la lista y ve el número 120. Lo mete en la variable time.
• Llega al if y el procesador se pregunta: ¿120 > 500?
• La respuesta electrónica es Falso (False).
• Acción de la máquina: Como dio falso, el circuito se salta la línea 41 
  (slow_count = slow_count + 1). 
  No gasta energía ahí. La alcancía se queda en 0.

🔹 Vuelta 2:

• La máquina se mueve al casillero 1 y toma el 640. Lo mete en time.
• Evalúa en el if: ¿640 > 500?
• La respuesta electrónica es Verdadero (True).
• Acción de la máquina: ¡Entra a la línea 41! El procesador va a la RAM, abre la cajita slow_count 
  (que tiene un 0), le suma 1 en su unidad aritmética, borra el valor viejo y guarda un 1.

🔹 Vuelta 3:

• Va al casillero 2, toma el 510 y lo mete en time.
• Evalúa en el if: ¿510 > 500?
• La respuesta es Verdadero (True).
• Acción de la máquina: Vuelve a entrar a la línea 41. Abre la cajita (que tiene un 1), le suma 1 y 
  ahora guarda un 2 en la memoria RAM.

🔹 Vuelta 4:

• Va al casillero 3, toma el 200 y lo mete en time.
• Evalúa en el if: ¿200 > 500?
• La respuesta es Falso (False).
• Acción de la máquina: Se salta la suma. La alcancía se mantiene intacta en 2.

🔹 Vuelta 5 (La última):

• Va al casillero 4, toma el último número, 999, y lo mete en time.
• Evalúa en el if: ¿999 > 500?
• La respuesta es Verdadero (True).
• Acción de la máquina: Entra a la línea 41 por última vez. Abre la cajita (que tiene un 2), 
  le suma 1 y la cierra dejando un 3 guardado.

🏁 Paso 3: El Reporte Final (Línea 8)

• El procesador se da cuenta de que ya no hay más casilleros en la lista response_times, así que 
  rompe el bucle for y se sale de la sangría (los espacios hacia adentro).
• Llega a la línea del print(slow_count).
• La máquina va a la memoria RAM una última vez, abre la cajita slow_count, extrae el número 3 
  que dejamos ahí, lo transforma en impulsos de luz/píxeles y te lo pinta en la pantalla de la 
  terminal.

¡Y listo! Eso es exactamente todo el "ajedrez" eléctrico que hace la computadora 🤓 en microsegundos 
  para darte el resultado. 🧠⚡️

""" 