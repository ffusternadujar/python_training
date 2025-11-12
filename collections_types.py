"""
TIPOS DE DATOS COLECCIONES EN PYTHON
=====================================

Este módulo introduce los tipos de datos contenedores o colecciones en Python.
Las colecciones permiten almacenar múltiples valores en una sola variable.

OBJETIVOS DE APRENDIZAJE:
- Entender qué son las colecciones y cuándo usarlas
- Conocer las características de cada tipo de colección
- Aprender a crear y manipular colecciones
- Comprender conceptos de mutabilidad, orden y unicidad

TIPOS PRINCIPALES DE COLECCIONES:
1. list (listas): Colección ordenada y mutable, permite duplicados
2. tuple (tuplas): Colección ordenada e inmutable, permite duplicados
3. set (conjuntos): Colección no ordenada y mutable, NO permite duplicados
4. dict (diccionarios): Colección de pares clave-valor, claves únicas

CONCEPTOS CLAVE:
- Mutable: Se puede modificar después de crear (list, set, dict)
- Inmutable: No se puede modificar después de crear (tuple)
- Ordenada: Mantiene el orden de inserción (list, tuple, dict)
- Indexable: Se puede acceder por posición (list, tuple)
"""

# =============================================================================
# 1. LISTAS (LIST)
# =============================================================================
# Las listas son la colección más versátil en Python
# Características: ORDENADAS, MUTABLES, PERMITEN DUPLICADOS, INDEXABLES
# Se definen con corchetes: [elemento1, elemento2, ...]

# Ejemplo 1: Lista homogénea (todos los elementos del mismo tipo)
student_grades = [8.5, 9.2, 7.8, 9.0, 8.8, 7.6, 9.5, 8.9, 8.4, 9.1]

# Operador de repetición (*) en listas
# Crea una NUEVA lista repitiendo los elementos N veces (copia superficial)
print(student_grades * 3)
# Salida esperada: [8.5, 9.2, 7.8, 9.0, 8.8, 7.6, 9.5, 8.9, 8.4, 9.1, 8.5, 9.2, ...]

# Ejemplo 2: Lista heterogénea (elementos de diferentes tipos)
# Python permite mezclar tipos: int, str, float, bool, otras listas, None, etc.
mixed_list = [10, "Hello", 9.5, True, "World", 7, False, 8.3, [1, 2, 3], None]

print(mixed_list)
# Salida esperada: [10, 'Hello', 9.5, True, 'World', 7, False, 8.3, [1, 2, 3], None]

print(mixed_list * 3)
# IMPORTANTE: El operador * hace una copia superficial (shallow copy)
# Si la lista contiene objetos mutables (como otras listas), se copian las referencias

# =============================================================================
# 2. RANGE (RANGOS)
# =============================================================================
# range() genera una secuencia inmutable de números
# Es "lazy" (evaluación perezosa): no genera todos los números en memoria
# Sintaxis: range(start, stop, step) - stop es EXCLUSIVO
# Características: INMUTABLE, INDEXABLE, EFICIENTE EN MEMORIA

number_range = range(1, 11)  # Genera números del 1 al 10 (11 es exclusivo)
print(list(number_range))    # Convertimos a lista para visualizar los valores
# Salida esperada: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# NOTA: range() es útil para bucles y no consume memoria por todos los números
# Para ver los valores, hay que convertirlo a lista con list()

# =============================================================================
# OPERACIONES COMUNES CON LISTAS (Ejemplos adicionales)
# =============================================================================

# Acceso por índice (comienza en 0)
print("Primera nota:", student_grades[0])    # Primera posición (índice 0)
# Salida esperada: Primera nota: 8.5

print("Última nota:", student_grades[-1])    # Última posición (índice -1)
# Salida esperada: Última nota: 9.1

# Slicing (rebanado) - obtener sublistas
print("Primeras 3 notas:", student_grades[0:3])  # Índices 0, 1, 2 (3 es exclusivo)
# Salida esperada: Primeras 3 notas: [8.5, 9.2, 7.8]

print("Últimas 3 notas:", student_grades[-3:])   # Últimos 3 elementos
# Salida esperada: Últimas 3 notas: [8.4, 9.1]

# Métodos comunes de listas (las listas son mutables)
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.append(7)           # Añade al final
# numbers ahora: [3, 1, 4, 1, 5, 9, 2, 6, 7]

numbers.insert(0, 0)        # Inserta en posición específica
# numbers ahora: [0, 3, 1, 4, 1, 5, 9, 2, 6, 7]

numbers.remove(1)           # Elimina la primera ocurrencia del valor
# numbers ahora: [0, 3, 4, 1, 5, 9, 2, 6, 7] (eliminó el primer 1)

numbers.sort()              # Ordena la lista in-place (modifica la original)
print("Lista ordenada:", numbers)
# Salida esperada: Lista ordenada: [0, 1, 2, 3, 4, 5, 6, 7, 9]

print("Longitud de la lista:", len(numbers))  # Número de elementos
# Salida esperada: Longitud de la lista: 9

# =============================================================================
# PUNTOS CLAVE PARA RECORDAR
# =============================================================================
# 1. Las listas son MUTABLES: se pueden modificar después de crearlas
# 2. Las listas son ORDENADAS: mantienen el orden de inserción
# 3. Las listas permiten DUPLICADOS: el mismo valor puede aparecer varias veces
# 4. Las listas pueden contener CUALQUIER TIPO de dato, incluso mezclados
# 5. range() es eficiente para generar secuencias, pero no es una lista
# 6. Los índices comienzan en 0, y los negativos cuentan desde el final

