def calcular_costo_matricula():
    # Solicitar las cuatro notas del estudiante
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    nota4 = float(input("Ingrese la cuarta nota: "))

    # Solicitar el costo total de la matrícula
    costo_matricula = float(input("Ingrese el costo total de la matrícula: "))

    # Calcular el promedio de las notas
    promedio = (nota1 + nota2 + nota3 + nota4) / 4

    # Determinar la clasificación de rendimiento
    if promedio >= 9.0:
        clasificacion = "Excelente"
        descuento = 0.20  # 20% de descuento
    else:
        clasificacion = "No Excelente"
        descuento = 0.00  # Sin descuento

    # Calcular el monto final a pagar por la matrícula
    costo_final = costo_matricula * (1 - descuento)

    # Mostrar resultados
    print(f"Promedio del estudiante: {promedio:.2f}")
    print(f"Clasificación de rendimiento: {clasificacion}")
    print(f"Monto final a pagar por la matrícula: {costo_final:.2f} unidades monetarias")

# Ejecutar la función
calcular_costo_matricula()

x, y, z, w = 15, 10, 20, 8

# Verificar si x está entre y y z
condicion1 = y < x < z

# Verificar si w es par
condicion2 = (w % 2 == 0)

# Mostrar resultados
print(f"x está entre y y z: {condicion1}")
print(f"w es par: {condicion2}")

a, b, c, d = 7, 5, 3, 3

# Verificar las condiciones
condicion = (a > b) != (c == d)

# Mostrar resultado
print(f"a es mayor que b o c es igual a d, pero no ambas condiciones: {condicion}")

x, y, z = -3, 5, 0

# Verificar las condiciones
condicion = (x < 0) and (y > 0) and (z == 0)

# Mostrar resultado
print(f"x es negativo, y es positivo, y z es cero: {condicion}")

