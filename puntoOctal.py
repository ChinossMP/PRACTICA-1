def puntoOctalADecimal(numero):
    izquierda = numero[:numero.find(".")]
    derecha =  numero[numero.find(".") + 1:]

    #convertir parte derecha
    izquierda = [int(digito) for digito in izquierda]
    izquierda.reverse()

    numDecimal = 0
    for i in range(len(izquierda)):
        numDecimal += (8**i) * izquierda[i]

    #parte derecha

    numDecimalDerecha = 0
    derecha = [int(digito) for digito in derecha]
    for i in range(1, len(derecha)+ 1, 1):
        numDecimalDerecha += derecha[i - 1] * (8 ** -i)


    print(numDecimal + numDecimalDerecha)

def puntoOctalBinario(numero):
    izquierda = numero[:numero.find(".")]
    derecha = numero[numero.find(".") + 1:]

    #parte izquierda
    equivalencias = [[0, 0, 0],
                     [0, 0, 1],
                     [0, 1, 0],
                     [0, 1, 1],
                     [1, 0, 0],
                     [1, 0, 1],
                     [1, 1, 0],
                     [1, 1, 1]]

    resultado = []
    izquierda = [int(digito) for digito in izquierda]
    for i in range(len(izquierda)):
        resultado.append(equivalencias[izquierda[i]])

    #Parde derecha

    resultadoDerecha = []
    derecha = [int(digito) for digito in derecha]
    for i in range(len(derecha)):
        resultadoDerecha.append(equivalencias[derecha[i]])

    print("Binario: ", end = "")
    for i in range(len(resultado)):
        for j in range(3):
            print(resultado[i][j], end="")
    print(".", end = "")
    for j in range(len(resultadoDerecha)):
        for k in range(3):
            print(resultadoDerecha[j][k], end="")


def puntoOctalHex(numero):
    izquierda = numero[:numero.find(".")]
    izquierda = [int(num) for num in izquierda]
    derecha = numero[numero.find(".") + 1:]
    derecha = [int(num) for num in derecha]

    #parte izquierda
    equivalenciasOctal = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

    equivalenciasHex = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1],
                        [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]

    resultadoBinario = []

    for i in range(len(izquierda)):
        resultadoBinario.append(equivalenciasOctal[izquierda[i]])

    binario = []
    for i in range(len(resultadoBinario)):
        for j in range(3):
            binario.append(resultadoBinario[i][j])

    binario.reverse()

    binarioHex = [0] * (len(izquierda) * 4)

    for i in range(len(binario)):
        binarioHex[i] = binario[i]

    binarioHex.reverse()

    sublistas = [binarioHex[i:i + 4] for i in range(0, len(binarioHex), 4)]

    numHexadecimal = []
    for i in range(len(sublistas)):
        for j in range(len(equivalenciasHex)):
            if sublistas[i] == equivalenciasHex[j]:
                if j == 10:
                    numHexadecimal.append("A")
                elif j == 11:
                    numHexadecimal.append("B")
                elif j == 12:
                    numHexadecimal.append("C")
                elif j == 13:
                    numHexadecimal.append("D")
                elif j == 14:
                    numHexadecimal.append("E")
                elif j == 15:
                    numHexadecimal.append("F")
                else:
                    numHexadecimal.append(j)

    binarioDerecha = []

    for i in range(len(derecha)):
        binarioDerecha.append(equivalenciasOctal[derecha[i]])

    formaBinaria = []
    for i in range(len(binarioDerecha)):
        for j in range(3):
            formaBinaria.append(binarioDerecha[i][j])

    llenarCeros = [0] * (len(derecha) * 4)

    for i in range(len(formaBinaria)):
        llenarCeros[i] = formaBinaria[i]

    subListasDerecha = [llenarCeros[i:i + 4] for i in range(0, len(llenarCeros), 4)]

    hexDerecha = []
    for i in range(len(subListasDerecha)):
        for j in range(len(equivalenciasHex)):
            if subListasDerecha[i] == equivalenciasHex[j]:
                if j == 10:
                    hexDerecha.append("A")
                elif j == 11:
                    hexDerecha.append("B")
                elif j == 12:
                    hexDerecha.append("C")
                elif j == 13:
                    hexDerecha.append("D")
                elif j == 14:
                    hexDerecha.append("E")
                elif j == 15:
                    hexDerecha.append("F")
                else:
                    hexDerecha.append(j)

    print("Hexadecimal: ", end="")
    for i in range(1, len(numHexadecimal), 1):
        print(numHexadecimal[i], end="")
    print(".", end="")
    for k in range(len(hexDerecha)):
        print(hexDerecha[k], end="")