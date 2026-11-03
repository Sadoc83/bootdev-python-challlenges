# =========================================================
# Día 16 - Validación de estados de viaje en Urban Routes
# =========================================================

# Contexto
# En Urban Routes, el equipo de QA necesita validar que la aplicación no muestre estados 
# no válidos en los viajes.
# Los estados no válidos definidos por el equipo son: "pendiente", “error".

# La tarea pide recorrer la lista de estados y verificar cada uno:
# Si el estado no es válido, muestra un mensaje de advertencia con su nombre.
# En cualquier otro caso, muestra que el estado es válido.

# Código inicial
# estados_de_viaje = ["completado", "en curso", "cancelado", "error"]
# estados_invalidos = ["pendiente", "error"]
 
# for estado in ...:
# 	if ...:
# print("Estado no válido encontrado:", ...)
# 	else:
# print("Estado válido:", ...)

# Pista
# Usaremos not in para comprobar que cada estado no está en la lista de estados_invalidos. 
# Si no está, entonces es válido; si está, muestra un mensaje de advertencia.

# Código final

estados_de_viaje = ["completado", "en curso", "cancelado", "error"]
estados_invalidos = ["pendiente", "error"]
 
for estado in estados_de_viaje:
	if estado in estados_invalidos:
		print("Estado no válido encontrado:", estado)
	else:
		print("Estado válido:", estado)

# Resultado
# Estado válido: completado
# Estado válido: en curso
# Estado válido: cancelado
# Estado no válido encontrado: error


# 🕵️‍♂️ Análisis de QA: ¿Cómo funciona este filtro?

# • La estrategia del if estado in estados_invalidos:
 
#   El bucle toma cada elemento de la lista original de viajes. 
#   Al llegar al cuarto elemento, estado vale "error". El condicional pregunta: 
#       ¿El texto "error" se encuentra dentro de la lista estados_invalidos?. 

#       Como la respuesta es Sí (True), imprime el mensaje de advertencia de forma exacta.