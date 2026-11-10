"""
# Proyecto del Día 3: Analizador de Texto (Udemy, Python Básico para quien NO sabe Python)

Este proyecto tiene como objetivo aplicar los conceptos aprendidos sobre strings, input, 
indexación y formateo de strings en Python. El programa permitirá al usuario ingresar un texto y 
luego elegir realizar diversas operaciones de análisis sobre ese texto.

## Consigna
Vas a crear un programa que le pida al usuario que ingrese un texto de al menos 10 palabras. 
Tu programa va a procesar ese texto, lo va a procesar, y le va a devolver un análisis detallado, 
que incluya:

1. Contar el número total de caracteres en el texto
2. Contar el número de caracteres sin incluir los espacios
3. Contar la cantidad de vocales que hay en el texto
4. Contar el número total de palabras en el texto ingresado

**nota**: para resolver los siguientes items, deberás investigar otros métodos de strings que no
hemos visto. Recuerda valerte de *type*, *dir* y *help*

5. Eliminar la primera palabra
6. Reemplazar todos los espacios por guiones medios (-)
8. Cambia las mayúsculas a minúsculas y las minúsculas a mayúsculas 

Al finalizar el procesamiento, se imprimirán 8 cadenas literales mostrando los resultados del 
análisis (una cadena por cada resultado).

"""
### Resolución

# Ingreso del usuario:

mensaje = input("Saludos Humano !!!... Escribe un texto, frase o sentencia que tenga al menos 10 palabras: ")


# 1. Contar el número total de caracteres en el texto

caracteres_totales = len(mensaje)
print(caracteres_totales)

# 2. Contar el número de caracteres sin incluir los espacios

caracteres_sin_espacios = mensaje.replace(" ","")
total_sin_espacios = len(caracteres_sin_espacios)
print(total_sin_espacios)

# 3. Contar la cantidad de vocales que hay en el texto

mensaje_minusculas = mensaje.lower()
a = mensaje_minusculas.count("a")
e = mensaje_minusculas.count("e")
i = mensaje_minusculas.count("i")
o = mensaje_minusculas.count("o")
u = mensaje_minusculas.count("u")
total_de_vocales = a + e + i + o + u
print(f"3. La cantidad de vocales encontradas en el texto es: {total_de_vocales}\n"
      f"   ↳ Desglose:\n"
      f"     a = {a} veces\n"
      f"     e = {e} veces\n"
      f"     i = {i} veces\n"
      f"     o = {o} veces\n"
      f"     u = {u} veces")

# 4. Contar el número total de palabras en el texto ingresado

lista_de_palabras = mensaje.split()
total_de_palabras = len(lista_de_palabras)
print(total_de_palabras)

# 5. Eliminar la primera palabra

palabras = mensaje.split()
palabras_restantes = palabras[1:]
mensaje_modificado = " ".join(palabras_restantes)
print(mensaje_modificado)

# 6. Reemplazar todos los espacios por guiones medios (-)

mensaje_con_guiones = mensaje.replace(" ","-")
print(mensaje_con_guiones)

# 7. Cambia las mayúsculas a minúsculas y las minúsculas a mayúsculas

mensaje_invertido = mensaje.swapcase()
print (mensaje_invertido)

# 8. Muéstrale al usuario los resultados del análisis de su texto.

print("\n=====================================================================")
print("📊 REPORTE DE ANÁLISIS DE TEXTO (PROYECTO DÍA 3) 📊")
print("=====================================================================\n")

# Cadena 1: Caracteres totales
print(f"1. El número total de caracteres en tu texto es de: {caracteres_totales} en total\n")

# Cadena 2: Caracteres sin espacios
print(f"2. Excluyendo los espacios en blanco, el texto tiene: {total_sin_espacios} caracteres puros\n")

# Cadena 3: Total de vocales
print(f"3. La cantidad de vocales encontradas en el texto es: {total_de_vocales} vocales\n"
      f"\n   ↳ Desglose:\n"
      f"\n     a = {a} veces\n"
      f"     e = {e} veces\n"
      f"     i = {i} veces\n"
      f"     o = {o} veces\n"
      f"     u = {u} veces\n")

# Cadena 4: Total de palabras

print(f"4. El número total de palabras que componen tu enunciado es: {total_de_palabras} palabras\n")

# Cadena 5: Texto sin la primera palabra
print(f"5. Texto modificado tras remover la primera palabra:\n \n\t'{mensaje_modificado}'\n")

# Cadena 6: Texto con guiones
print(f"6. Formato de cadena con espacios sustituidos por guiones:\n \n\t{mensaje_con_guiones}\n")

# Cadena 7: Texto invertido (Swapcase)
print(f"7. Resultado del intercambio espejo entre mayúsculas y minúsculas:\n \n\t{mensaje_invertido}\n")

# Cadena 8: Mensaje de cierre del sistema
print(f"\n8. ¡Análisis finalizado con éxito para el usuario! Gracias por utilizar el sistema.\n")
print("=====================================================================")

# Paso de seguridad obligatorio para la Cadena 1
caracteres_totales = len(mensaje)

"""
¿Cómo quitarle lo "encimado" a tu reporte final?

Para darle un formato limpio, estilizado y con "aire" al Analizador de Texto, podemos usar 
tres técnicas muy sencillas:

    1. print() vacíos: Poner un print() sin nada adentro genera un renglón en blanco que separa 
        visualmente los bloques de texto.
    
    2. Líneas divisorias: Usar guiones (---) o iguales (===) crea secciones claras para el ojo humano.
    
    3. Tabuladores (\t): Así como \n es un Enter, \t es un Tabulador (un salto de 4 espacios a la derecha). 
        Sirve para crear sangrías y que los desgloses se vean escalonados de forma perfecta.
"""

# =====================================================================
# REPORTE "MAQUILLADO" Y ESPACIADO (Dashboard Estilo QA)
# =====================================================================
print("\n" + "="*70)
print(" 📊  REPORTE COMPLETO: ANALIZADOR DE TEXTO  📊")
print("="*70 + "\n")

# Cadena 1: Caracteres totales
print(f"🔹 1. TOTAL DE CARACTERES EN EL TEXTO:")
print(f"      ↳ {caracteres_totales} caracteres (contando espacios).\n")

# Cadena 2: Caracteres sin espacios
print(f"🔹 2. CARACTERES PUROS:")
print(f"      ↳ {total_sin_espacios} caracteres (excluyendo espacios).\n")

# Cadena 3: Total de vocales con desglose tabulado (\t)
print(f"🔹 3. CONTEO DE VOCALES GENERAL:")
print(f"      ↳ Total: {total_de_vocales} vocales encontradas.")
print(f"        [ Desglose por letra ]")
print(f"\t• a = {a} veces")
print(f"\t• e = {e} veces")
print(f"\t• i = {i} veces")
print(f"\t• o = {o} veces")
print(f"\t• u = {u} veces\n")

# Cadena 4: Total de palabras
print(f"🔹 4. TOTAL DE PALABRAS:")
print(f"      ↳ El texto contiene: {total_de_palabras} palabras.\n")

# Cadena 5: Sin la primera palabra
print(f"🔹 5. TEXTO TRUNCADO (Sin primera palabra):")
print(f"      ↳ \"{mensaje_modificado}\"\n")

# Cadena 6: Espacios por guiones
print(f"🔹 6. FORMATO DE CADENA (Con guiones):")
print(f"      ↳ {mensaje_con_guiones}\n")

# Cadena 7: Swapcase
print(f"🔹 7. EFECTO ESPEJO (Inversión de mayúsculas/minúsculas):")
print(f"      ↳ {mensaje_invertido}\n")

# Cadena 8: Mensaje de cierre final
print("="*70)
print(f"✅ 8. ¡PROCESAMIENTO FINALIZADO DE FORMA EXITOSA! SISTEMA EN ESPERA.")
print("="*70 + "\n")

"""

🕵️‍♂️ ¿Por qué este formato es superior?

• El uso de \n y los \n inline al final de los textos le dan "aire" a la terminal para que 
  los ojos del profesor no se cansen.
• El truco \t alinea perfectamente las viñetas (•) del desglose de las vocales, haciendo que 
  parezca una tabla estructurada de base de datos.
• Al usar print("\n" + "="*70), Python multiplica el carácter por 70, creando una barra divisoria 
  matemática perfecta sin que tengas que teclear 70 veces el signo.

"""