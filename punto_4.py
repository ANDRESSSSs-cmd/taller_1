# Solicitar las cuatro notas del estudiante
nota1 = float(input("Ingrese la primera nota (1-5): "))
nota2 = float(input("Ingrese la segunda nota (1-5): "))
nota3 = float(input("Ingrese la tercera nota (1-5): "))
nota4 = float(input("Ingrese la cuarta nota (1-5): "))

# Solicitar el costo total de la matrícula
costo_matricula = float(input("Ingrese el costo total de la matrícula: "))

# Calcular el promedio de las notas
promedio = (nota1 + nota2 + nota3 + nota4) / 4

# Determinar la clasificación del rendimiento
if 4 <= promedio <= 5:
    clasificacion = "Excelente"
    descuento = 0.20
elif 3 <= promedio < 4:
    clasificacion = "Bien"
    descuento = 0.00
else:
    clasificacion = "Deficiente"
    descuento = 0.00

# Calcular el monto final a pagar por la matrícula
monto_final = costo_matricula * (1 - descuento)

# Mostrar resultados
print(f"\nPromedio del estudiante: {promedio:.2f}")
print(f"Clasificación de rendimiento: {clasificacion}")
print(f"Monto final a pagar por la matrícula: ${monto_final:.2f}")
