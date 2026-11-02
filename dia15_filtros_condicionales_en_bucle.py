# =========================================================
# Día 15 - Implementar filtros condicionales en bucle interativo
# =========================================================

# En Urban Routes, el equipo de QA está revisando el estado de múltiples viajes 
# y quiere un resumen detallado al final.

# Completa el bucle for para:

# Declarar correctamente el bucle usando una variable para recorrer la lista.
# Usar esa variable dentro del cuerpo del bucle para:

# Mostrar el estado de cada viaje.
# Contar cuántos viajes están "en curso".
# Contar cuántos viajes están “pausado".

# Al final, muestra un resumen con ambos conteos.


# Código inicial
estados_de_viaje = ["en curso", "pausado", "finalizado", "en curso", "pausado", "en curso"]
en_curso = 0
pausados = 0

for estado in estados_de_viaje:
    print("Estado del viaje:", estado)
    if estado == "en curso":
        en_curso = en_curso + 1
    if estado == "pausado":
        pausados = pausados + 1        
# print("Resumen de QA:")
# print("Viajes en curso:", en_curso)
# print("Viajes pausados:", pausados)

# 🕵️‍♂️ Aquí tenemos un caso clásico de comparación de tipos de datos incorrectos dentro del bucle. 
# Es la razón exacta por la cual la terminal te arrojó 0 en ambos conteos al final.
# Si se mira con atención tus condicionales if, estás comparando la variable estado 
# (que guarda textos como "en curso" o "pausado") contra las variables en_curso y pausados 
# (que guardan números como 0). Como el texto "en curso" nunca va a ser igual al número 0, 
# Python ignora las sumas y las alcancías se quedan vacías.
# Además, en la línea 11 el código se quedó incompleto (if estado == pausados:). 
# Vamos a estructurarlo correctamente.

# 🛠️ Código Corregido y Explicado

# Para que las "alcancías" sumen de verdad, se debe comparar la variable -estado- directamente 
# contra las cadenas de texto exactas entre comillas ("en curso" y "pausado"):

# Código final

estados_de_viaje = ["en curso", "pausado", "finalizado", "en curso", "pausado", "en curso"]
en_curso = 0
pausados = 0

for estado in estados_de_viaje:
    print("Estado del viaje:", estado)
    if estado == "en curso":
        en_curso = en_curso + 1
    if estado == "pausado":
        pausados = pausados + 1
print("Resumen de QA:")
print("Viajes en curso:", en_curso)
print("Viajes pausados:", pausados)

# Resultado

# Resumen de QA:
# Viajes en curso: 3
# Viajes pausados: 2


# 🕵️‍♂️ Análisis de QA: ¿Por qué esto funciona correctamente?

# 1. Comparación de Texto (String vs String): Al escribir if estado == "en curso":, 
#    Python ahora sí puede validar de forma correcta. En la primera vuelta, estado vale "en curso". 
#    Como "en curso" == "en curso" es Verdadero (True), entra al bloque y le suma uno a la alcancía.

# 2. El Cierre del Bucle: Al corregir las dos condiciones y cerrar la línea de los pausados, 
#    el bucle procesará los 6 elementos de la lista en orden.

# 3. Resultado Esperado Real: Al correr esta versión, la terminal te arrojará el conteo 
#    analizado de forma impecable:
# 
# Resumen de QA:
# Viajes en curso: 3
# Viajes pausados: 2