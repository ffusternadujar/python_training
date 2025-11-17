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

student_grades = list(range(1, 10, 2))  # Números del 1 al 9 con paso 2
print(student_grades)  # Salida esperada: [1, 3, 5, 7, 9]

# =============================================================================
# 3. LISTAS Y OPERACIONES BÁSICAS
# =============================================================================
# Las listas permiten almacenar múltiples valores y calcular estadísticas fácilmente
student_grades = [9.1, 8.8, 7.5]

average = sum(student_grades) / len(student_grades)  # Calcula la media de las notas
print("Average grade:", average)  # Salida esperada: Average grade: 8.466666666666667

# =============================================================================
# 4. DICCIONARIOS (DICT)
# =============================================================================
# Los diccionarios almacenan pares clave-valor, útiles para asociar nombres con valores
student_grades = {"Alice": 9.1, "Bob": 8.8, "Charlie": 7.5}
print(student_grades.get("Alice")) # Salida esperada: 9.1

mean_grade = sum(student_grades.values()) / len(student_grades)  # Media de las notas usando los valores del diccionario
print("Mean grade:", mean_grade)  # Salida esperada: Mean grade: 8.466666666666667

# =============================================================================
# 5. TUPLAS (TUPLE)
# =============================================================================
# Las tuplas son colecciones inmutables, útiles para datos que no deben cambiar
monday_temperatures = (22.5, 24.0, 19.8, 21.5) # Temperaturas del lunes. Las tuplas son inmutables
