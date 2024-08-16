def decimalAOctal(numero):
    octal = []

    condicion = True

    while condicion == True:
        numero = numero / 8

        if (int(numero) == 0):
            condicion = False

        decimal = numero % 1
        auxiliar = decimal * 8
        numero = int(numero)

        octal.append(auxiliar)
    print("Octal: ", end="")
    octal.reverse()
    for i in range(len(octal)):
        print(int(octal[i]), end = "")

def decimalAHexadecimal(numero):
    hexadecimal = []

    condicion = True

    while condicion == True:
        numero = numero / 16

        if (int(numero) == 0):
            condicion = False

        decimal = numero % 1
        auxiliar = decimal * 16
        numero = int(numero)

        if (auxiliar == 10):
            hexadecimal.append("A")
        elif (auxiliar == 11):
            hexadecimal.append("B")
        elif (auxiliar == 12):
            hexadecimal.append("C")
        elif (auxiliar == 13):
            hexadecimal.append("D")
        elif (auxiliar == 14):
            hexadecimal.append("E")
        elif (auxiliar == 15):
            hexadecimal.append("F")
        else:
            hexadecimal.append(int(auxiliar))
    print("Hexadecimal: ", end = "")
    hexadecimal.reverse()
    for i in range (len(hexadecimal)):
        print(hexadecimal[i], end = "")


def decimalABinario(numero):
    binario = []
    condicion = True

    while condicion == True:
        numero = numero / 2
        if (numero.is_integer()):
            binario.append(0)
        else:
            binario.append(1)
            if (numero == 0.5):
                condicion = False
            numero = int(numero)
    print("Binario: ", end="")
    binario.reverse()
    for i in range(len(binario)):
        print(binario[i], end = "")