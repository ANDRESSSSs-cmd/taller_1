def calcular_costo_llamada():
    # Solicitar destino
    destino = input("Ingrese el destino de la llamada (local, nacional, internacional): ").strip().lower()

    # Solicitar duración
    duracion = float(input("Ingrese la duración de la llamada en minutos: "))

    # Establecer tarifas por minuto
    tarifas = {
        "local": 1.00,
        "nacional": 2.00,
        "internacional": 5.00
    }

    # Determinar la tarifa por minuto
    if destino in tarifas:
        tarifa_por_minuto = tarifas[destino]
    else:
        print("Destino no válido.")
        return

    # Calcular el costo total
    costo_total = duracion * tarifa_por_minuto

    # Aplicar descuento si es necesario
    if duracion > 15:
        costo_total *= 0.80  # Aplicar 20% de descuento

    # Mostrar el costo total
    print(f"El costo total de la llamada es: {costo_total:.2f} unidades monetarias")

# Ejecutar la función
calcular_costo_llamada()




