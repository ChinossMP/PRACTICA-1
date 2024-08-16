def binAOctal(digitos):
    # Convertir de binario a octa

    equivalenciasOctal = [[0, 0, 0],
                          [0, 0, 1],
                          [0, 1, 0],
                          [0, 1, 1],
                          [1, 0, 0],
                          [1, 0, 1],
                          [1, 1, 0],
                          [1, 1, 1]]

    # dividir para encontrar el múltiplo
    multiplo = [digitos[i:i + 3] for i in range(0, len(digitos), 3)]

    llenarConCeros = [0] * (len(multiplo) * 3)

    # voltear los digitos

    for i in range(len(digitos)):
        llenarConCeros[i] = digitos[i]

    llenarConCeros.reverse()
    # dividir en grupos de tres

    subListas = [llenarConCeros[i:i + 3] for i in range(0, len(llenarConCeros), 3)]

    octal = []
    # comparar con la equivalencia
    for i in range(len(subListas)):
        for j in range(len(equivalenciasOctal)):
            if subListas[i] == equivalenciasOctal[j]:
                octal.append(j)

    print("Octal: ", end="")
    for i in range(len(octal)):
        print(octal[i], end = "")


def binAHex(digitos):
    # de binario a hexadecimal

    equivalenciasHex = [[0, 0, 0, 0],
                        [0, 0, 0, 1],
                        [0, 0, 1, 0],
                        [0, 0, 1, 1],
                        [0, 1, 0, 0],
                        [0, 1, 0, 1],
                        [0, 1, 1, 0],
                        [0, 1, 1, 1],
                        [1, 0, 0, 0],
                        [1, 0, 0, 1],
                        [1, 0, 1, 0],
                        [1, 0, 1, 1],
                        [1, 1, 0, 0],
                        [1, 1, 0, 1],
                        [1, 1, 1, 0],
                        [1, 1, 1, 1]]
    # dividir para encontrar multiplo
    digitosBin = [digitos[i: i + 4] for i in range(0, len(digitos), 4)]

    llenarCeros = [0] * (len(digitosBin) * 4)

    # llenar con los dígitos al reves

    for i in range(len(digitos)):
        llenarCeros[i] = digitos[i]

    llenarCeros.reverse()

    subListas = [llenarCeros[i:i + 4] for i in range(0, len(llenarCeros), 4)]

    hex = []
    for i in range(len(subListas)):
        for j in range(len(equivalenciasHex)):
            if subListas[i] == equivalenciasHex[j]:
                if j == 10:
                    hex.append("A")
                elif j == 11:
                    hex.append("B")
                elif j == 12:
                    hex.append("C")
                elif j == 13:
                    hex.append("D")
                elif j == 14:
                    hex.append("E")
                elif j == 15:
                    hex.append("F")
                else:
                    hex.append(j)

    print("Hexadecimal: ", end="")
    for i in range(len(hex)):
        print(hex[i], end = "")

def binADecimal(digitos):
    suma = 0
    digitos.reverse()
    for i in range(len(digitos)):
        suma += digitos[i] * (2 ** i)

    print(suma)
