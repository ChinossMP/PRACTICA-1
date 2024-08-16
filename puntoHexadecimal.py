import re
import Hexadecimal


def hexDecimal(numero):
    izquierda = numero[:numero.find(".")]
    digitosIzquierda = []
    for i in izquierda:
        digitosIzquierda.append(i)


    derecha = numero[numero.find(".") + 1:]
    digitosDerecha = []
    for i in derecha:
        digitosDerecha.append(i)
    #parte izquierda
    for i in range(len(digitosIzquierda)):
        if digitosIzquierda[i] == 'A':
            digitosIzquierda[i] = 10
        elif digitosIzquierda[i] == 'B':
            digitosIzquierda[i] = 11
        elif digitosIzquierda[i] == 'C':
            digitosIzquierda[i] = 12
        elif digitosIzquierda[i] == 'D':
            digitosIzquierda[i] = 13
        elif digitosIzquierda[i] == 'E':
            digitosIzquierda[i] = 14
        elif digitosIzquierda[i] == 'F':
            digitosIzquierda[i] = 15

    digitosIzquierda.reverse()
    digitosIzquierda = [int(digito) for digito in digitosIzquierda]

    numeroDecimal = 0
    for i in range(len(digitosIzquierda)):
        numeroDecimal += (16 ** i) * digitosIzquierda[i]

    #parte derecha
    for i in range(len(digitosDerecha)):
        if digitosDerecha[i] == 'A':
            digitosDerecha[i] = 10
        elif digitosDerecha[i] == 'B':
            digitosDerecha[i] = 11
        elif digitosDerecha[i] == 'C':
            digitosDerecha[i] = 12
        elif digitosDerecha[i] == 'D':
            digitosDerecha[i] = 13
        elif digitosDerecha[i] == 'E':
            digitosDerecha[i] = 14
        elif digitosDerecha[i] == 'F':
            digitosDerecha[i] = 15

    digitosDerecha = [int(digito) for digito in digitosDerecha]

    numeroDecimalDerecha = 0
    for i in range(1,len(digitosDerecha)+ 1,1):
        numeroDecimalDerecha += (16 ** -i) * digitosDerecha[i - 1]


    print(numeroDecimal + numeroDecimalDerecha)

def hexBinario(numero):
    izquierda = numero[:numero.find(".")]
    derecha = numero[numero.find(".") + 1:]

    digitosIzquierda = []
    for i in range(len(izquierda)):
        digitosIzquierda.append(izquierda[i])

    digitosDerecha = []
    for i in range(len(derecha)):
        digitosDerecha.append(derecha[i])

    #parte izquierda
    equivalenciasHex = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1],
                        [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]

    #Parte derecha

    for i in range(len(digitosDerecha)):
        if digitosDerecha[i] == 'A':
            digitosDerecha[i] = 10
        elif digitosDerecha[i] == 'B':
            digitosDerecha[i] = 11
        elif digitosDerecha[i] == 'C':
            digitosDerecha[i] = 12
        elif digitosDerecha[i] == 'D':
            digitosDerecha[i] = 13
        elif digitosDerecha[i] == 'E':
            digitosDerecha[i] = 14
        elif digitosDerecha[i] == 'F':
            digitosDerecha[i] = 15

    hexDerecha = []
    digitosDerecha = [int(dig) for dig in digitosDerecha]

    for i in range(len(digitosDerecha)):
        hexDerecha.append(equivalenciasHex[digitosDerecha[i]])

    print("Binario: ", end = "")
    Hexadecimal.hexABin(digitosIzquierda)
    print(".", end="")
    for k in range(len(hexDerecha)):
        for l in range(4):
            print(hexDerecha[k][l], end = "")

def hexAOctal(numero):
    izquierda = numero[:numero.find(".")]
    derecha = numero[numero.find(".") + 1:]

    digitosIzquierda = []
    for i in range(len(izquierda)):
        digitosIzquierda.append(izquierda[i])
    digitosDerecha = []
    for i in range(len(derecha)):
        digitosDerecha.append(derecha[i])
    #########################Parte derecha###########################3

    equivalenciasHex = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1],
                        [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
                        [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
    equivalenciasOctal = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

    for i in range(len(digitosDerecha)):
        if digitosDerecha[i] == 'A':
            digitosDerecha[i] = 10
        elif digitosDerecha[i] == 'B':
            digitosDerecha[i] = 11
        elif digitosDerecha[i] == 'C':
            digitosDerecha[i] = 12
        elif digitosDerecha[i] == 'D':
            digitosDerecha[i] = 13
        elif digitosDerecha[i] == 'E':
            digitosDerecha[i] = 14
        elif digitosDerecha[i] == 'F':
            digitosDerecha[i] = 15

    hexABin = []
    digitosDerecha = [int(dig) for dig in digitosDerecha]

    for i in range(len(digitosDerecha)):
        hexABin.append(equivalenciasHex[digitosDerecha[i]])

    vectorBinario = []
    for i in range(len(hexABin)):
        for j in range(4):
            vectorBinario.append(hexABin[i][j])

    vecAux = vectorBinario

    # Agregar los ceros faltantes
    sublistas = [vectorBinario[i:i + 3] for i in range(0, len(vectorBinario), 3)]
    binarioOctal = [0] * (len(sublistas) * 3)
    for i in range(len(vecAux)):
        binarioOctal[i] = vecAux[i]

    digitosBin = [binarioOctal[i: i + 3] for i in range(0, len(binarioOctal), 3)]

    numOctal = []

    for i in range(len(digitosBin)):
        for j in range(len(equivalenciasOctal)):
            if digitosBin[i] == equivalenciasOctal[j]:
                numOctal.append(j)

    print("Octal: ", end = "")
    digitosIzquierda.reverse()
    Hexadecimal.hexAOctal(digitosIzquierda)
    print(".", end = "")
    for i in range(len(numOctal)):
        print(numOctal[i], end = "")
