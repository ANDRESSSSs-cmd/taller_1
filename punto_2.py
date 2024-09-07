def calcular_costo(tarifa, minutos):
    return tarifa * minutos


def main():
    tarifas = {
        "Estados Unidos": 900,
        "Canadá": 800,
        "Europa": 950,
        "Resto del mundo": 1250
    }

    print("Tarifas por minuto de llamadas internacionales:")
    for pais, tarifa in tarifas.items():
        print(f"{pais}: {tarifa} pesos")

    # Solicitar al usuario el destino y los minutos
    destino = input("Ingrese el destino de la llamada (Estados Unidos, Canadá, Europa, Resto del mundo): ")
    minutos = float(input("Ingrese la duración de la llamada en minutos: "))

    # Verificar si el destino está en el diccionario de tarifas
    if destino in tarifas:
        costo = calcular_costo(tarifas[destino], minutos)
        print(f"El costo de la llamada a {destino} es: {costo:.2f} pesos")
    else:
        print("Destino no reconocido. Por favor, elija uno de los destinos listados.")


if __name__ == "__main__":
    main()
