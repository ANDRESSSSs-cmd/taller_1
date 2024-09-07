def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso y la altura.

    :param peso: Peso en kilogramos
    :param altura: Altura en metros
    :return: IMC calculado
    """
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero.")
    imc = peso / (altura ** 2)
    return imc


def mostrar_resultado(imc):
    """
    Muestra el resultado del IMC con un mensaje interpretativo.

    :param imc: IMC calculado
    """
    print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")

    if imc < 18.5:
        print("Usted está bajo de peso.")
    elif 18.5 <= imc < 24.9:
        print("Usted tiene un peso normal.")
    elif 25 <= imc < 29.9:
        print("Usted tiene sobrepeso.")
    else:
        print("Usted tiene obesidad.")


def main():
    """
    Función principal que solicita al usuario el peso y la altura, calcula el IMC y muestra el resultado.
    """
    try:
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))

        # Validar entradas
        if peso <= 0:
            raise ValueError("El peso debe ser mayor que cero.")
        if altura <= 0:
            raise ValueError("La altura debe ser mayor que cero.")

        # Calcular el IMC
        imc = calcular_imc(peso, altura)

        # Mostrar el resultado
        mostrar_resultado(imc)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
