"""
OPERACIONES CON LISTAS EN PYTHON
==================================

Este módulo practica las operaciones y métodos más comunes con listas.
Las listas son colecciones mutables (modificables) y ordenadas.

OBJETIVOS DE APRENDIZAJE:
- Aprender los métodos principales de listas
- Entender cómo modificar listas (mutabilidad)
- Practicar indexación, slicing y búsqueda
- Comprender la diferencia entre métodos y funciones built-in

MÉTODOS CUBIERTOS:
1. append() - Añade un elemento al final
2. clear() - Vacía la lista
3. index() - Busca la posición de un elemento
4. __getitem__() / indexación - Accede a elementos
5. Slicing - Extrae sublistas
6. Índices negativos - Acceso desde el final
7. len() - Obtiene la longitud
8. join() - Combina strings con separador
"""

# =============================================================================
# 1. MÉTODO APPEND() - AÑADIR ELEMENTOS
# =============================================================================
# append() añade un elemento al FINAL de la lista
# Modifica la lista original (operación in-place)
# Devuelve None (no retorna la lista modificada)

monday_temperaures = [22.5, 24.0, 19.8, 21.5]  # Temperaturas del lunes

monday_temperaures.append(23.0)  # Añadimos una nueva temperatura al final de la lista
print(monday_temperaures)  # Las listas son mutables
# Salida esperada: [22.5, 24.0, 19.8, 21.5, 23.0]

# =============================================================================
# 2. MÉTODO CLEAR() - VACIAR LA LISTA
# =============================================================================
# clear() elimina TODOS los elementos de la lista
# Deja la lista vacía pero sigue existiendo
# También es una operación in-place

monday_temperaures.clear()  # Vaciamos la lista
print(monday_temperaures)
# Salida esperada: []

# =============================================================================
# 3. MÉTODO INDEX() - BUSCAR LA POSICIÓN DE UN ELEMENTO
# =============================================================================
# index() busca la PRIMERA ocurrencia de un elemento
# Devuelve el índice (posición) del elemento
# Lanza ValueError si el elemento no existe
# Sintaxis: list.index(element, start, end)

monday_temperaures = [22.5, 24.0, 19.8, 21.5]  # Restauramos la lista original
print(monday_temperaures.index(19.8))  # Devuelve el índice del primer elemento con valor 19.8
# Salida esperada: 2 

# Ejemplo: Buscar un elemento empezando desde una posición específica
# print(monday_temperaures.index(22.5, 2))  # Busca 22.5 empezando desde el índice 2
# Salida esperada: ValueError (porque 22.5 no está en índice 2 o posteriores)

# =============================================================================
# 4. INDEXACIÓN Y ACCESO A ELEMENTOS
# =============================================================================
# Podemos acceder a elementos usando []
# Índices van de 0 (primer elemento) hasta len(lista)-1 (último)
# También se puede usar __getitem__() (equivalente interno)

print(monday_temperaures.__getitem__(1))  # Equivalente a monday_temperaures[1], devuelve el elemento en el índice 1
print(monday_temperaures[1])  # Salida esperada: 24.0

# =============================================================================
# 5. FUNCIÓN LEN() - OBTENER LA LONGITUD
# =============================================================================
# len() devuelve el número total de elementos en la lista

print(len(monday_temperaures))  # Devuelve el número de elementos en la lista

# =============================================================================
# 6. SLICING - EXTRACTOR DE SUBLISTAS
# =============================================================================
# Slicing permite extraer porciones (sublistas) de una lista
# Sintaxis: lista[inicio:fin:paso]
# - inicio: índice donde comienza (incluido)
# - fin: índice donde termina (EXCLUSIVO)
# - paso: incremento entre elementos (por defecto 1)

print(monday_temperaures[1:3])  # Slicing: devuelve una sublista desde el índice 1 hasta el 3 (exclusivo)

print(monday_temperaures[:2])  # Desde el inicio hasta el índice 2 (exclusivo)
# Salida esperada: [22.5, 24.0]

print(monday_temperaures[2:])  # Desde el índice 2 hasta el final
# Salida esperada: [19.8, 21.5]

# =============================================================================
# 7. ÍNDICES NEGATIVOS - ACCESO DESDE EL FINAL
# =============================================================================
# Los índices negativos acceden a elementos desde el final de la lista
# -1 es el último elemento, -2 es el penúltimo, etc.

print(monday_temperaures[-1])  # Índice negativo: último elemento de la lista
# Salida esperada: 21.5

print(monday_temperaures[-3:-1])  # Slicing con índices negativos (desde -3 hasta -1 exclusivo)
# Salida esperada: [24.0, 19.8]

# =============================================================================
# 8. SLICING CON PASO (STEP)
# =============================================================================
# El tercer parámetro en slicing es el paso (step)
# Permite saltar elementos: [inicio:fin:paso]

print(monday_temperaures[0:4:2])  # Slicing con step: desde el índice 0 hasta el 4 (exclusivo) con paso 2

# =============================================================================
# 9. ACCESO A ELEMENTOS DENTRO DE ELEMENTOS (ANIDACIÓN)
# =============================================================================
# Las listas pueden contener otros tipos de datos, incluyendo strings
# Podemos acceder a caracteres dentro de strings en la lista

my_string_list = ['hello', 'world']
print(my_string_list[0][1])  # Acceso al segundo carácter del primer string de la lista
# Salida esperada: 'e' (segundo carácter de 'hello')

# =============================================================================
# 10. MÉTODO JOIN() - CONCATENAR ELEMENTOS CON SEPARADOR
# =============================================================================
# join() es un método de strings que combina los elementos de una lista
# Se usa cuando la lista contiene strings
# Sintaxis: separador.join(lista_de_strings)

cool_list = ['H', 'e', 'l', 'l', 'o']
print(str.join("---", cool_list))
# Salida esperada: H---e---l---l---o