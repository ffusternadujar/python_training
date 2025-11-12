"""
TIPOS DE DATOS SIMPLES EN PYTHON
==================================

Este módulo introduce los tipos de datos primitivos fundamentales en Python.
Los tipos simples son los bloques de construcción básicos para almacenar valores individuales.

OBJETIVOS DE APRENDIZAJE:
- Entender qué son los tipos de datos y por qué son importantes
- Conocer los 4 tipos simples principales: int, float, str, bool
- Aprender a declarar variables y realizar operaciones básicas
- Comprender el sistema de tipado dinámico de Python

TIPOS CUBIERTOS:
1. int (enteros): Números enteros sin decimales
2. float (flotantes): Números con decimales
3. str (cadenas): Texto y caracteres
4. bool (booleanos): Valores de verdad (True/False)
"""

# =============================================================================
# 1. TIPO INTEGER (ENTEROS)
# =============================================================================
# Los enteros son números sin parte decimal: ..., -2, -1, 0, 1, 2, ...
# Se usan para contar, indexar, operaciones matemáticas exactas, etc.
items = 2      # Número de artículos (entero)
price = 120    # Precio por artículo (entero)

# Operaciones aritméticas básicas: +, -, *, /, //, %, **
total_amount = items * price  # Multiplicación de enteros resulta en entero
print("total amount = ", total_amount)
# Salida esperada: total amount = 240

# =============================================================================
# 2. TIPO FLOAT (FLOTANTES/DECIMALES)
# =============================================================================
# Los float representan números con parte decimal usando punto flotante.
# Se usan para mediciones, cálculos científicos, valores monetarios precisos, etc.
# NOTA: Los float tienen precisión limitada y pueden tener errores de redondeo.
weight = 0.75  # Peso en kilogramos (float)
height = 1.80  # Altura en metros (float)

# Ejemplo práctico: Cálculo del Índice de Masa Corporal (BMI)
# Fórmula: BMI = peso(kg) / altura(m)²
# El operador ** es para potencias/exponenciación
bmi = weight / (height ** 2)
print("BMI = ", bmi)
# Salida esperada: BMI = 0.23148148148148148

# =============================================================================
# 3. TIPO STRING (CADENAS DE TEXTO)
# =============================================================================
# Los strings son secuencias de caracteres encerradas en comillas (' o ")
# Se usan para texto, nombres, mensajes, rutas de archivos, etc.
# Python es DINÁMICAMENTE TIPADO: las anotaciones de tipo son solo hints,
# no se aplican en tiempo de ejecución.
x: str = 10     # Anotamos x como str, pero asignamos un int (¡Python lo permite!)
y: int = "20"   # Anotamos y como int, pero asignamos un str (¡Python lo permite!)

# Las anotaciones de tipo NO se aplican en tiempo de ejecución. Python es dinámicamente tipado.
# El tipo real de una variable se determina por el valor asignado, no por la anotación.

# print(x + y)  # Esto lanzaría TypeError: unsupported operand type(s) for +: 'int' and 'str'
                # No se pueden sumar directamente un número y un string

print(x + x)  # Esto funciona: 10 + 10 = 20 (suma de enteros)
# Salida esperada: 20

print(y + y)  # Esto funciona: "20" + "20" = "2020" (concatenación de strings)
# Salida esperada: 2020

# =============================================================================
# 4. TIPO BOOLEAN (BOOLEANOS)
# =============================================================================
# Los booleanos representan valores de verdad: True (verdadero) o False (falso)
# Se usan para condiciones, flags, control de flujo, lógica, etc.
# Operadores lógicos: and (y), or (o), not (no)

is_active = True   # Usuario activo
is_admin = False   # Usuario NO es administrador

print("is_active =", is_active)
# Salida esperada: is_active = True

print("is_admin =", is_admin)
# Salida esperada: is_admin = False

# Operador 'and': devuelve True solo si AMBOS operandos son True
print("is_active and is_admin =", is_active and is_admin)
# Salida esperada: is_active and is_admin = False
# (porque is_admin es False)

# =============================================================================
# EJERCICIO 1: COERCIÓN DE TIPOS Y ARITMÉTICA MIXTA
# =============================================================================
# OBJETIVO: Observar cómo Python maneja operaciones con tipos mixtos (int + float)
# INSTRUCCIONES: Ejecuta el código y observa el resultado
# PREGUNTA: ¿Qué tipo tiene el resultado? ¿Por qué?

x = 2      # int
y = 4.6    # float
z = 5      # int

result = x + y + z  # Suma de int + float + int
print("result = ", result)
# Salida esperada: result = 11.6
# El resultado es float porque al sumar int + float, Python convierte todo a float

# LECCIÓN CLAVE: En operaciones mixtas, Python convierte al tipo más "amplio" (int → float)
