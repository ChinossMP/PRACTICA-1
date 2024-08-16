

def decimalHexPunto(numero):
    # de decimal a hexadecimal

    parteEntera = int(numero)
    parteDecimal = numero - parteEntera

    hex = []
    condicion = True

    while condicion == True:
        parteEntera = parteEntera / 16

        if (int(parteEntera) == 0):
            condicion = False

        decimal = parteEntera % 1
        auxiliar = decimal * 16
        parteEntera = int(parteEntera)

        hex.append(auxiliar)

    hex.reverse()
    hexDecimal = []
    presicion = 10
    for i in range(presicion):
        parteDecimal *= 16
        entero = int(parteDecimal)
        hexDecimal.append(int(parteDecimal))
        parteDecimal = parteDecimal - entero

    # juntar las dos partes
    for i in range(len(hex)):
        if hex[i] == 10:
            print('A', end="")
        elif hex[i] == 11:
            print('B', end="")
        elif hex[i] == 12:
            print('C', end="")
        elif hex[i] == 13:
            print('D', end="")
        elif hex[i] == 14:
            print('E', end="")
        elif hex[i] == 15:
            print('F', end="")
        else:
            print(int(hex[i]), end="")
    print(".", end="")
    for i in range(len(hexDecimal)):
        if hexDecimal[i] == 10:
            print('A', end="")
        elif hexDecimal[i] == 11:
            print('B', end="")
        elif hexDecimal[i] == 12:
            print('C', end="")
        elif hexDecimal[i] == 13:
            print('D', end="")
        elif hexDecimal[i] == 14:
            print('E', end="")
        elif hexDecimal[i] == 15:
            print('F', end="")
        else:
            print(int(hexDecimal[i]), end="")


def decimalOctalPunto(numero):
    parteEntera = int(numero)
    parteDecimal = numero - parteEntera
    # octal de la parte entera
    octal = []

    condicion = True

    while condicion == True:
        parteEntera = parteEntera / 8

        if (int(parteEntera) == 0):
            condicion = False

        decimal = parteEntera % 1
        auxiliar = decimal * 8
        parteEntera = int(parteEntera)

        octal.append(auxiliar)

    octal.reverse()

    # parte decimal a octal

    ocDecimal = []
    presicion = 10
    for i in range(presicion):
        entero = 0
        parteDecimal *= 8
        entero = int(parteDecimal)
        ocDecimal.append(int(parteDecimal))
        parteDecimal = parteDecimal - entero

    # Juntar las dos partes
    for i in range(len(octal)):
        print(int(octal[i]), end="")
    print(".", end="")
    for i in range(len(ocDecimal)):
        print(ocDecimal[i], end="")


def decimalBinarioPunto(numero):
    parteEntera = int(numero)
    parteDecimal = numero - parteEntera

    # Binario de la parte entera
    binario = []
    condicion = True

    while condicion == True:
        parteEntera = parteEntera / 2
        if (parteEntera.is_integer()):
            binario.append(0)
        else:
            binario.append(1)
            if (parteEntera == 0.5):
                condicion = False
            parteEntera = int(parteEntera)

    binario.reverse()

    # Binario de la parte decimal

    binDecimal = []
    presicion = 10
    for i in range(presicion):
        parteDecimal *= 2
        entero = int(parteDecimal)
        binDecimal.append(int(parteDecimal))
        parteDecimal = parteDecimal - entero

    # Juntar parte entera con parte decimal
    for i in range(len(binario)):
        print(binario[i], end="")

    print(".", end="")

    for i in range(len(binDecimal)):
        print(binDecimal[i], end="")