"""
OPERACIONES CON DICCIONARIOS EN PYTHON
========================================

Este módulo practica las operaciones y métodos más comunes con diccionarios.
Los diccionarios son colecciones mutables que almacenan pares clave-valor.

OBJETIVOS DE APRENDIZAJE:
- Aprender a acceder a valores en diccionarios
- Entender las estructuras clave-valor
- Practicar métodos de diccionarios
- Comprender cuándo usar diccionarios sobre listas

CONCEPTOS CLAVE:
- Las claves deben ser únicas
- Los valores pueden ser cualquier tipo de dato
- Los diccionarios mantienen orden de inserción (desde Python 3.7+)
- Son mutables: se pueden modificar después de crear

MÉTODOS CUBIERTOS:
1. Indexación directa [clave] - Accede a un valor
2. get() - Accede a un valor de forma segura
3. values() - Obtiene todos los valores
4. keys() - Obtiene todas las claves
5. items() - Obtiene pares clave-valor
"""

# =============================================================================
# 1. CREAR UN DICCIONARIO Y ACCEDER A VALORES
# =============================================================================
# Los diccionarios almacenan datos como pares clave-valor
# Se definen con llaves: {clave1: valor1, clave2: valor2, ...}
# Las claves son únicas dentro del diccionario

student_grades = {"Alice": 9.1, "Bob": 8.8, "Charlie": 7.5}

# Acceso directo usando la clave entre corchetes
print(student_grades["Alice"])  # Accede al valor asociado a la clave "Alice"
# Salida esperada: 9.1

# =============================================================================
# 2. ACCEDER A LOS VALORES Y CALCULAR ESTADÍSTICAS
# =============================================================================
# values() retorna TODOS los valores del diccionario
# Permite calcular operaciones como suma, promedio, etc.

# Convertimos a lista para acceder por índice
print(list(student_grades.values())[1])  # Obtiene el segundo valor del diccionario
# Salida esperada: 8.8